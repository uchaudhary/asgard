import os

count = 0

from flask import (Flask, Response, flash, redirect, render_template, request,
                   url_for)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"


def createApp():
    app = Flask(__name__)
    app.config.from_mapping(
        # https://flask.palletsprojects.com/en/2.1.x/config/ for Configuration Options
        UPLOAD_FOLDER=UPLOAD_FOLDER,
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            if "file" not in request.files:
                flash("No file part")
                return redirect(request.url)
            file = request.files["file"]
            print(type(request))
            if file.filename == "":
                flash("No selected file")
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                flash("File Uploaded Successfully")
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = createApp()
    app.debug = True
    app.run()
