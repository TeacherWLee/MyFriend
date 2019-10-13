"""


"""

__author__ = "Li Wei (liw@sicnu.edu.cn)"


from . import web
from flask import render_template


@web.route("/index")
def index():
    return render_template("index.html")
