from pkg import repository_analysis


def main():
    print("あなたのユーザ名は？")
    user_name = input()
    print("対象リポジトリは？")
    repository_name = input()
    repository_analysis.merge(user_name, repository_name)


main()

