from pkg import analysis_git
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask('__name__')
CORS(app)

app.config['JSON_AS_ASCII'] = False


@app.route("/", methods=["GET"])
def get_log():
    git_name = request.args.get("gitName")
    if git_name == "":
        return jsonify({'message': 'header owner name is null'}), 400

    repository_name = request.args.get("repositoryName")
    if repository_name == "":
        return jsonify({'message': 'header repository name is null'}), 400

    # git_log = analysis_git.analysis_git_log(git_name, repository_name)
    git_message, git_time, git_diff = analysis_git.analysis_git_log(git_name, repository_name)
    return jsonify({"git_message": git_message, "git_time": git_time, "git_diff": git_diff}), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)

