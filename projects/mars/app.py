from flask import Flask, render_template, request, jsonify
from pythonprac.dbprac import db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    print(request.form)
    name_receive = request.form['name']
    address_receive = request.form['address']
    size_receive = request.form['size']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    mars = list(db.mars.find({}, {'_id': False}))
    return jsonify({'mars': mars})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
