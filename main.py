from pkg import determine_time
from pkg import get_repository_log

print("あなたのユーザ名は？")
userName = input()
print("対象リポジトリは？")
repositoryName = input()
get_repository_log.GetRipositoryLog(userName, repositoryName)
determine_time.Timebetweencommits()