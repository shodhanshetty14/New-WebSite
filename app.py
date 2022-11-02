from flask import Flask,render_template
import requests
from details import API_KEY



app = Flask(__name__)

# class News_Data():
#     pass

@app.route("/")
def News():
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': "Technology",
        "country": 'in',
        "apiKey": API_KEY
    }
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []
    for data in arti:
        result.append({
            # "author" : data['author'],
            "title" : data["title"],
            "description" : data["description"],
            "content" : data["content"],
            "link" : data['url'],
            "image" : data['urlToImage']
            })
    return render_template('new_body.html', result = result)



if __name__ == "__main__":
    app.run(debug=True)
