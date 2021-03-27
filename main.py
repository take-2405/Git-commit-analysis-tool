from pkg import analysis_git
from flask import Flask, jsonify, request

app = Flask("git-analysis")


@app.route("/get/log", methods=["GET"])
def get_log():
    git_name = request.args.get("gitName")
    repository_name = request.args.get("repositoryName")
    analysis_git.analysis_git_log(git_name, repository_name)
    return "aaaa"

app.run(port=8080)

