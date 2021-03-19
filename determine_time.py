import datetime


def Timebetweencommits():
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
