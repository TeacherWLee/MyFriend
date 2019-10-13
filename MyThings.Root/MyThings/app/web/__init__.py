"""


"""

__author__ = "Li Wei (liw@sicnu.edu.cn)"


from flask import Blueprint

web = Blueprint("web", __name__, url_prefix="/")

from . import home
