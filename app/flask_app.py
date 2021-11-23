from flask import Flask
from flask_cors import CORS

from app.routes import events, federal_reserve, futures, yields

application = Flask(__name__)
app = application
app.config['JSON_SORT_KEYS'] = False
CORS(app)

app.register_blueprint(futures.blueprint)
app.register_blueprint(events.blueprint)
app.register_blueprint(yields.blueprint)
app.register_blueprint(federal_reserve.blueprint)


@app.route("/")
def healthcheck():
    return "ok"
