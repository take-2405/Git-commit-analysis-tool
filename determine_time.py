import datetime
path = './result/user.txt'
f = open(path, 'r')
data = f.read()
f.close()

# 目的の情報を書き出すためのテキスト作成
path = './result/user_time.txt'
f = open(path, 'w')

for i in range(0,len(data),27):
    year = int(data[i:i+4])
    month = int(data[i+5:i+7])
    day = int(data[i+8:i+10])
    hour = int(data[i+11:i+13])
    minute = int(data[i+14:i+16])
    second = int(data[i+17:i+19])
    # print(minute,second)
    print(data[17:19])
    commit_date_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    f.write(str(commit_date_time) + "\n")
    # break
f.close()