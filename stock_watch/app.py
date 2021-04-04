from flask import Flask, render_template, url_for

from controllers.manufacturer_controller import manufacturers_blueprint
from controllers.fabric_controller import fabrics_blueprint


app = Flask(__name__)


app.register_blueprint(fabrics_blueprint)
app.register_blueprint(manufacturers_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)