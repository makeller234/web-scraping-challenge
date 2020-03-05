from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_deets = mongo.db.collection.find_one()
    return render_template("index.html", mars_deets=mars_deets)


@app.route("/scrape")
def scraper():
    mars_deets = mongo.db.mars_deets
    mars_deets_data = scrape_mars.scrape()
    mars_deets.update({}, mars_deets_data, upsert=True)
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)