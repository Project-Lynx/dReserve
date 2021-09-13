from flask import Flask

from app.routes import events, futures, yields

application = Flask(__name__)
app = application

app.register_blueprint(futures.blueprint)
app.register_blueprint(events.blueprint)
app.register_blueprint(yields.blueprint)


@app.route("/")
def healthcheck():
    return "ok"
