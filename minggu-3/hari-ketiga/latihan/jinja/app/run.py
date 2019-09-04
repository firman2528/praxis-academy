from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)



@app.template_filter()
def datetimefilter(value, format='%Y%m%d %H:%M') :
    # CONVERT A DATETIME TO A DIFFERENT FORMAT
    return value.strftime(format)
    
app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def template_test() :
    return render_template("template.html", my_string="Wheeee !", my_list=[0,1,2,3,4,5], title="Firman Yuspriyadi")


@app.route("/home")
def home() :
    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="Home", current_time=datetime.now())

@app.route("/about")
def about() :
    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="About", current_time=datetime.now())

@app.route("/contact")
def contact() :
    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="Contact", current_time=datetime.now())


if __name__ == '__main__' :
    app.run(debug=True)