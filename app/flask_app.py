from flask import Flask
from flask_cors import CORS

from app.routes import events, futures, yields

application = Flask(__name__)
app = application
CORS(app)

app.register_blueprint(futures.blueprint)
app.register_blueprint(events.blueprint)
app.register_blueprint(yields.blueprint)


@app.route("/")
def healthcheck():
    return "ok"
