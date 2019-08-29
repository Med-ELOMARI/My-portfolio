# -*- encoding: utf-8 -*-
"""
Fully Coded App by AppSeed.us
License: commercial
Read more at https://appseed.us/pricing
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template
# all the imports necessary
from werkzeug.exceptions import abort

from app import app


# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:

        # try to match the pages defined in -> themes/phantom/pages/
        return render_template('layouts/default.html',
                               content=render_template('pages/' + path))
    except:
        abort(404)


def http_err(err_code):
    err_msg = 'Oups !! Some internal error ocurred. Thanks to contact support.'

    if 400 == err_code:
        err_msg = "It seems like you are not allowed to access this link."

    elif 404 == err_code:
        err_msg = "The URL you were looking for does not seem to exist."
        err_msg += "<br /> Define the new page in templates/pages"

    elif 500 == err_code:
        err_msg = "Internal error. Contact the manager about this."

    else:
        err_msg = "Forbidden access."

    return err_msg


@app.errorhandler(401)
def e401(e):
    return http_err(401)  # "It seems like you are not allowed to access this link."


@app.errorhandler(404)
def e404(e):
    return http_err(404)  # "The URL you were looking for does not seem to exist.<br><br>
    # If you have typed the link manually, make sure you've spelled the link right."


@app.errorhandler(500)
def e500(e):
    return http_err(500)  # "Internal error. Contact the manager about this."


@app.errorhandler(403)
def e403(e):
    return http_err(403)  # "Forbidden access."


@app.errorhandler(410)
def e410(e):
    return http_err(410)  # "The content you were looking for has been deleted."
