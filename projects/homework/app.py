from flask import Flask, render_template, request, jsonify
from pythonprac.dbprac import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    print(request.form)
    id = request.form['id_receive']
    comment = request.form['comment_receive']

    doc = {
        'id': id,
        'comment': comment
    }

    db.comment.insert_one(doc)

    print(id, comment)
    return jsonify({'msg': '응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comments = list(db.comment.find({}, {"_id": False}))
    return jsonify({'comments': comments})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)