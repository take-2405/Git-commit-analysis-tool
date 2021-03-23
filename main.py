from pkg import analysis_git
from flask import Flask, jsonify, request

app = Flask("git-analysis")


@app.route("/get/log", methods=["GET"])
def get_log():
    # if not request.headers.get("Content-Type") == 'application/json':
    #     error_message = {
    #         'error': 'not supported Content-Type'
    #     }
    #     return jsonify(error_message), 400
    git_name = request.headers.get("gitName")
    repository_name = request.headers.get("repositoryName")
    analysis_git.analysis_git_log(git_name, repository_name)
    return request.headers.get("gitName")

app.run(port=8080)

