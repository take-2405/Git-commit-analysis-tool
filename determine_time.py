import datetime
compare_flag = False
compare_datetime = datetime.datetime(year=1, month=1, day=1, hour=1)

path = './result/user.txt'
f = open(path, 'r')
data = f.read()
f.close()

# 目的の情報を書き出すためのテキスト作成
path = './result/user_time.txt'
f = open(path, 'w')

for i in range(0, len(data)):
    if data[i] == "2" and data[i+1] == "0" and data[i+2] == "2":
        # print(i)
        for j in range(i, len(data)):
            # print(data[i:i + 4])
            year = int(data[i:i + 4])
            month = int(data[i + 5:i + 7])
            day = int(data[i + 8:i + 10])
            hour = int(data[i + 11:i + 13])
            minute = int(data[i + 14:i + 16])
            second = int(data[i + 17:i + 19])
            commit_date_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute,
                                                 second=second)
            f.write(str(commit_date_time) + "\n")
            if compare_flag:
                print(compare_date_time - commit_date_time)
                compare_datetime = commit_date_time
                break;
            else:
                compare_date_time = commit_date_time
                compare_flag = True
                break;
    else:
        i=i+1
f.close()