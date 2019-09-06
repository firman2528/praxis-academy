from app import app
from flask import render_template, request, redirect
from datetime import datetime
from werkzeug import secure_filename
from flask import send_from_directory
import os
from flask import abort
from flask import request


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

app.config["MAX_IMAGE_FILESIZE"] = 50*1024*1024
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG"]
app.config["UPLOAD_FOLDER"] = "static/uploads"
basedir = os.path.abspath(os.path.dirname(__file__))


@app.errorhandler(404) 
def page_not_found(e) :
    app.logger.info(f'Page not found : {request.url}')
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(403) 
def forbidden(e) :
    return render_template("error_hanlders/handler.html"), STATUS_CODE

@app.errorhandler(500)
def server_error(e) :
    # email_admin(message="Server error", url=request.url, error=e)
    app.logger.error(f"Server error  : {request.url}")
    return render_template("error_handlers/500.html"), 500

def allowed_image_filesize(filesize) :
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"] :
        return True
    else :
        return False

def allowed_images(filename) :
    if not "." in filename :
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"] :
        return True
    else :
        return False


@app.route("/")
def index() :
    return render_template("public/index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload() :
    print(os.path.join(app.config["UPLOAD_FOLDER"]))
    if request.method == 'POST' :
        if request.files :
            print(request)
            img = request.files["image"]

            if img.filename == "" :
                print("No Filename")
                return redirect(request.url)

            
            if allowed_images(img.filename) :
                filename = secure_filename(img.filename)

                img.save(os.path.join(basedir, app.config["UPLOAD_FOLDER"], filename))
                print("image saved")
                return redirect(request.url)
            else :
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("public/upload.html")

@app.route("/about")
def about() :
    return "All about Flask"

@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz) :
    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")

    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/profile/<username>")
def profile(username) :
    user = None
    for username in users :
        user = users[username]

    return render_template("public/dynamic.html", username=username, user=user)


@app.route("/sign-up",methods=["GET", "POST"])
def sign_up() :
    if request.method == "POST" :
        req = request.form 

        missing = list()

        for k, v in req.items():
            if v == "" :
                missing.append(k)

        if missing :
            feedback = f"Missing fields for {'.'.join(missing)}"
            return render_template("public/sign_up.html", feedback = feedback)
        
        username = req.get("username")
        email = req["email"]
        password = request.form["password"]



        return redirect(request.url)
    return render_template("public/sign_up.html")

@app.route("/jinja")
def jinja() :
    myname="Firman"
    # Strings
    my_name = "Julian"

    # Integers
    my_age = 30

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    my_html ="<h1>This some HTML<h1>"

    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"


    return render_template("public/jinja.html", my_name=myname,
            my_age=my_age, langs=langs,friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
            my_remote=my_remote, suspicious=suspicious, my_html=my_html, date=date, repeat=repeat)

@app.template_filter("clean_date")
def clean_date(dt) :
    return dt.strftime("%d %b %Y")


@app.route('/json', methods=['POST'])
def json_example() :
    return "Thanks"



