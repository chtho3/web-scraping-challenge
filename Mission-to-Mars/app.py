from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars")



@app.route("/")
def index():
    mars_scrape = mongo.mars_db.mars_scrape.find_one()

    return render_template("index.html", mars_scrape=mars_scrape)


@app.route("/scrape")
def scraper():
    mars_scrape = mongo.mars_db.mars_scrape
    mars_scrape_data = scrape_mars.scrape()
    mars_scrape.update({}, mars_scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=False)
