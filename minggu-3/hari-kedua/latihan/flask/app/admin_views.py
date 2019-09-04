from app import app
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboar() :
    return render_template("admin/dashboard.html")

