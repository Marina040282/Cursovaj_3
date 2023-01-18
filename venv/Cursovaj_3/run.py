from flask import Flask, send_from_directory

from app.posts.views import posts_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(posts_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
