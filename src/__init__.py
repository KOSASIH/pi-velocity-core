from flask import Flask

# import application modules
from src.configure_app import configure_app, register_blueprints

# initialize the Flask app
app = Flask(__name__)

# configure the Flask app
configure_app(app)

# register Flask Blueprints
register_blueprints(app)

# run the Flask app
if __name__ == "__main__":
    app.run()
