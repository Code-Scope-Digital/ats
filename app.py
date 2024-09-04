from flask import Flask
from db import init_db

from csd.route import csd_bp

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

#Initialize the database
mongo = init_db(app)


with app.app_context():
    app.register_blueprint(csd_bp)

if __name__ == '__main__':
    app.run(debug=True,port=5000)