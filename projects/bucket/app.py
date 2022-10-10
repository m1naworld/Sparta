from flask import Flask, render_template, request, jsonify
from pythonprac.dbprac import db


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    content_receive = request.form['content_give']

    bucket = list(db.bucket.find({}, {"_id": False}))
    num = len(bucket) + 1

    doc = {
        'num': num,
        'content': content_receive,
        'done': 0
    }

    db.bucket.insert_one(doc)

    return jsonify({'msg': '기록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = int(request.form['num_give'])
    # 주의!! request.form을 통해 들어온 값은 모두 문자!!
    print(type(num_receive))
    db.bucket.update_one({'num': num_receive}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'bucket_list': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)