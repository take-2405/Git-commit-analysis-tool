import os
import requests

def GetRipositoryLog(userName,repositoryName):
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