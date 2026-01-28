from fastapi import FastAPI
from flask import render_template

from user_database import data

app = FastAPI()


@app.get("/")
def main():
    """Entry point; the view for the main page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('main.html', cities=cities)


@app.get("/hello/{name}")
def main_plot():
    """The view for rendering the scatter chart"""
    img = get_main_image()
    response = send_file(img, mimetype='image/png')
    get_headers(response)
    return response

