from flask import Flask, render_template, request, jsonify
from pythonprac.dbprac import db
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url']
    star_receive = request.form['star']
    comment_receive = request.form['comment']

    print(url_receive, star_receive, comment_receive)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    description = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': title,
        'image': image,
        'description': description,
        'star': star_receive,
        'comment': comment_receive
    }

    print(doc)

    db.movies.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movies = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movies})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)