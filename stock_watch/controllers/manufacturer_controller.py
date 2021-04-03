from flask import Flask, render_template, url_for
from flask import Blueprint


manufacturers_blueprint = Blueprint("manufacturers", __name__)