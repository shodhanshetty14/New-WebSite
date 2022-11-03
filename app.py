from flask import Flask,render_template
import requests
from details import API_KEY



app = Flask(__name__)

# class News_Data():
#     pass

@app.route("/")
def Tech_News():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        "category": "Technology",
        "language": "en",
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('technology.html', result = result)


@app.route("/business")
def Business_News():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "business",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('business.html', result = result)


@app.route("/politics")
def Politic_News():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "politics",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('politics.html', result = result)


@app.route("/sports")
def sports_News():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "sports",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('sports.html', result = result)


@app.route("/entertainment")
def Entertainment_news():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "entertainment",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('entertainment.html', result = result)


@app.route("/health")
def Health_news():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "health",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('health.html', result = result)


@app.route("/science")
def Science_news():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "science",
        "language": 'en',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            # "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('science.html', result = result)


if __name__ == "__main__":
    app.run(debug=True)
