import os
import requests
import datetime


def GetLogUnText(userName,repositoryName):
    # 日付が2つ重複しているので1つを表示しないためのフラグ
    date_flag = True
    # コミットメッセージの終わりを識別するためのフラグ
    message_flag = False

    # プライベートリポジトリを調べるためにtokenを読み込む
    # parameter = {'access_token': os.environ['Git_Path']}
    # 目的のリポジトリのログを取得
    # site = requests.get("https://api.github.com/repos/take-2405/Git-commit-analysis-tool/commits", params=parameter)
    site = requests.get("https://api.github.com/repos/"+userName+"/"+repositoryName+"/commits")
    siteInfo = site.text
    # 目的の情報を書き出すためのテキスト作成
    path = './result/user.txt'
    f = open(path, 'w')

    # 目的のログ部分を切り取る
    for i in range(0, len(siteInfo)):
        # 日時を選別
        if siteInfo[i] == "d" and siteInfo[i + 1] == "a" and siteInfo[i + 2] == "t" and siteInfo[i + 3] == "e":
            if date_flag:
                f.write(siteInfo[i + 7:i + 26] + "\n")
                i = i + 27
                date_flag = False
            else:
                date_flag = True
        # メッセージを選別
        if siteInfo[i] == "m" and siteInfo[i + 1] == "e" and siteInfo[i + 2] == "s" and siteInfo[i + 3] == "s" and \
                siteInfo[i + 4] == "a" and siteInfo[i + 5] == "g" and siteInfo[i + 6] == "e":
            message_start = i + 10
            for message_end in range(message_start, len(siteInfo)):
                if siteInfo[message_end] == "\"":
                    if message_flag:
                        f.write(siteInfo[message_start:message_end - 2] + "\n")
                        message_flag = False
                        break;
                    else:
                        message_flag = True
    f.close()

def timebetweencommitsUnText():
    compare_flag = False
    path = './result/user.txt'
    f = open(path, 'r')
    data = f.read()
    f.close()

    # 目的の情報を書き出すためのテキスト作成
    path = './result/user_time.txt'
    f = open(path, 'w')

    for i in range(0, len(data)):
        if data[i] == "2" and data[i + 1] == "0" and data[i + 2] == "2":
            for j in range(i, len(data)):
                year = int(data[j:j + 4])
                month = int(data[j + 5:j + 7])
                day = int(data[j + 8:j + 10])
                hour = int(data[j + 11:j + 13])
                minute = int(data[j + 14:j + 16])
                second = int(data[j + 17:j + 19])
                commit_date_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute,
                                                     second=second)
                i = j
                if compare_flag:
                    f.write(str(compare_date_time - commit_date_time)+"\n")
                    compare_date_time = commit_date_time
                else:
                    compare_date_time = commit_date_time
                    compare_flag = True
                f.write(str(commit_date_time) + "\n")
                break;
        else:
            i = i + 1
    f.close()


def merge(user_name, repository_name):
    # 日付が2つ重複しているので1つを表示しないためのフラグ
    date_flag = True
    # コミットメッセージの終わりを識別するためのフラグ
    message_flag = False
    # 日付比較のフラグ
    compare_flag = False
    # 目的のリポジトリのログを取得
    site = requests.get("https://api.github.com/repos/" + user_name + "/" + repository_name + "/commits")
    site_info = site.text
    # 目的のログ部分を切り取る
    for i in range(0, len(site_info)):
        # 日時を選別
        if site_info[i] == "d" and site_info[i + 1] == "a" and site_info[i + 2] == "t" and site_info[i + 3] == "e":
            if date_flag:
                # i = i+6
                for j in range(i, len(site_info)):
                    if site_info[j] == "2" and site_info[j + 1] == "0" and (site_info[j + 2] == "1" or site_info[j + 2] == "2"):
                    # if site_info[j] == "2" and site_info[j + 1] == "0" and site_info[j + 2] == "2":
                        year = int(site_info[j:j + 4])
                        month = int(site_info[j + 5:j + 7])
                        day = int(site_info[j + 8:j + 10])
                        hour = int(site_info[j + 11:j + 13])
                        minute = int(site_info[j + 14:j + 16])
                        second = int(site_info[j + 17:j + 19])
                        commit_date_time = datetime.datetime(year=year, month=month, day=day, hour=hour,
                                                             minute=minute,
                                                             second=second)
                        i = j
                        if compare_flag:
                            print(str(commit_date_time)+" 次コミットとの時間差："+str(compare_date_time - commit_date_time))
                            # print(str(compare_date_time - commit_date_time))
                            compare_date_time = commit_date_time
                        else:
                            compare_date_time = commit_date_time
                            compare_flag = True
                            print(str(commit_date_time))
                        break;
                i = i + 27
                date_flag = False
            else:
                date_flag = True

        # メッセージを選別
        if site_info[i] == "m" and site_info[i + 1] == "e" and site_info[i + 2] == "s" and site_info[
        i + 3] == "s" and site_info[i + 4] == "a" and site_info[i + 5] == "g" and site_info[i + 6] == "e":
            message_start = i + 10
            for message_end in range(message_start, len(site_info)):
                if site_info[message_end] == "\"":
                    if message_flag:
                        print(site_info[message_start:message_end - 2]+"\n")
                        message_flag = False
                        break;
                    else:
                        message_flag = True