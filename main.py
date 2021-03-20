from pkg import determine_time
from pkg import get_repository_log
from pkg import getlog_untext

print("あなたのユーザ名は？")
userName = input()
print("対象リポジトリは？")
repositoryName = input()
getlog_untext.merge(userName, repositoryName)
# get_repository_log.GetRipositoryLog(userName, repositoryName)
# determine_time.Timebetweencommits()