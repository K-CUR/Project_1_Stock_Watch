from flask import Flask

app = Flask(__name__)

from controllers.fabric_controller import fabric_controller
from controllers.manufacturer_controller import manufacturer_controller

if __name__ == "__main__":
    app.run(debug=True)