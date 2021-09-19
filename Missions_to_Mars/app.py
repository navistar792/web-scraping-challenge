from flask import Flask, render_template, redirect, request, jsonify, Markup
from flask_pymongo import PyMongo
import scrape_mars
import json
import pandas as pd

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
    mars_1 = list(mongo.db.collection.find())
    print(mars_1)
    # render the html table
    df3 = pd.DataFrame(mars_1[0]['4']['table'], index=None)
    df4 = pd.DataFrame(df3.T)
    html_1 = df4.to_html(classes='table table-sm table-responsive table-striped table-hover ')
    html_2 = Markup(html_1)
    return render_template("index.html", mars=mars_1, html_1=html_2)


@app.route("/scrape")
def scrape():
    # Run the scrape function from the scrape_mars.py file
    mars_data = scrape_mars.scrape_info()

    # with open('troubleshooting_app.json', 'w') as json_file:
    #    json.dump(mars_data, json_file)
    
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

        # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
