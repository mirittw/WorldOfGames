from flask import Flask
import Utils

app = Flask(__name__)

@app.route('/scores', methods=['GET', 'POST', 'DELETE'])
def score_server():
    try:
        scores = open(Utils.SCORES_FILE_NAME, "r")
        fullscore = 0
        for line in scores.readlines():
            if line != "" and line != "\n":
                fullscore += int(line)
        return ('<html>' + '\n' +
                '<head>' + '\n' +
                '<title>Scores Game</title>' + '\n' +
                '</head>' + '\n' +
                '<body>' + '\n' +
                f'<h1>The score is <div id="score">{fullscore}</div></h1>' + '\n' +
                '</body>' + '\n' +
                '</html>')
    except BaseException as e:
        return ('<html>' + '\n' +
            '<head>' + '\n' +
            '<title>Scores Game</title>' + '\n' +
            '</head>' + '\n' +
            '<body>' + '\n' +
            f'<h1><div id="score" style="color:red">{e.args}</div></h1>' + '\n' +
            '</body>' + '\n' +
            '</html>')


app.run(host="0.0.0.0", port=5001, debug=True)
