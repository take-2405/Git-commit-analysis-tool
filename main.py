from pkg import analysis_git
from flask import Flask, jsonify, request

app = Flask('__name__')

app.config['JSON_AS_ASCII'] = False

@app.route("/get/log", methods=["GET"])
def get_log():
    git_name = request.args.get("gitName")
    if git_name == "":
        return jsonify({'message': 'header owner name is null'}), 400
    repository_name = request.args.get("repositoryName")
    if repository_name == "":
        return jsonify({'message': 'header repository name is null'}), 400
    git_log = analysis_git.analysis_git_log(git_name, repository_name)
    return jsonify({"git_log": git_log}), 200


if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0', port=8080)
    app.run(debug=False)

