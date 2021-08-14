from flask import Flask

from app.routes import futures

application = Flask(__name__)
app = application

app.register_blueprint(futures.blueprint)


@app.route("/")
def healthcheck():
    return "ok"
