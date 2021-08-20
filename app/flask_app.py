from flask import Flask

from app.routes import events, futures

application = Flask(__name__)
app = application

app.register_blueprint(futures.blueprint)
app.register_blueprint(events.blueprint)


@app.route("/")
def healthcheck():
    return "ok"
