import requests
import datetime


def analysis_git_log(user_name, repository_name):
    git_log = []
    # 日付が2つ重複しているので1つを表示しないためのフラグ
    date_flag = True
    # コミットメッセージの終わりを識別するためのフラグ
    message_flag = False
    # 日付比較のフラグ
    compare_flag = False
    # マージ判定フラグ
    merge_flag = False
    # 目的のリポジトリのログを取得
    site = requests.get("https://api.github.com/repos/" + user_name + "/" + repository_name + "/commits")
    # 目的のログ部分を切り取る
    for i in range(0, len(site.text)):
        # メッセージを選別
        if site.text[i] == "m" and site.text[i + 1] == "e" and site.text[i + 2] == "s" \
                and site.text[i + 3] == "s" and site.text[i + 4] == "a" and site.text[i + 5] == "g" and site.text[i + 6] == "e":
            message_start = i + 10
            for message_end in range(message_start, len(site.text)):
                if site.text[message_end] == "\"":
                    if message_flag:
                        git_log.append(site.text[message_start:message_end - 2])
                        message_flag = False
                        break;
                    else:
                        message_flag = True
        # 日時を選別
        if site.text[i] == "d" and site.text[i + 1] == "a" and site.text[i + 2] == "t" and site.text[i + 3] == "e" and site.text[i + 4] == "\"":
            if date_flag:
                i = i+6
                for j in range(i, len(site.text)):
                    if site.text[j] == "2" and site.text[j + 1] == "0" and (site.text[j + 2] == "0" or site.text[j + 2] == "1" or site.text[j + 2] == "2"):
                        year = int(site.text[j:j + 4])
                        month = int(site.text[j + 5:j + 7])
                        day = int(site.text[j + 8:j + 10])
                        hour = int(site.text[j + 11:j + 13])
                        minute = int(site.text[j + 14:j + 16])
                        second = int(site.text[j + 17:j + 19])
                        commit_date_time = datetime.datetime(year=year, month=month, day=day, hour=hour,
                                                             minute=minute,
                                                             second=second)
                        i = j
                        if compare_flag:
                            git_log.append(" 次コミットとの時間差："+str(compare_date_time - commit_date_time))
                            git_log.append(str(commit_date_time))
                            compare_date_time = commit_date_time
                            i = i + 27
                        else:
                            compare_date_time = commit_date_time
                            compare_flag = True
                            git_log.append(str(commit_date_time))
                            i = i + 27
                        break;
                date_flag = False
            else:
                i = i + 27
                date_flag = True
    return git_log
