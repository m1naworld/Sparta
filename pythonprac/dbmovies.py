import dbprac

db = dbprac.db

movie = db.movies.find_one({'title': '가버나움'})
star = movie['star']

all_movies = list(db.movies.find({'star': star}, {'_id': False}))

for movie in all_movies:
    if(movie['title'] == '가버나움'):
        db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})

    print(db.movies.find_one({'title': '가버나움'}))