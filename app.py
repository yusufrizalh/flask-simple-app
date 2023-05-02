from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey2023"


# set session
@app.route("/page/<int:value>")
def session1(value):
    session["myvalue"] = value
    return "Success to set value"


# display session
@app.route("/page/display")
def displaySession1():
    try:
        data = session["myvalue"]
        return "Set value is {}".format(data)
    except:
        return "Session is not set"


# destroy session
@app.route("/page/logout")
def logoutSession1():
    session.pop("myvalue")
    return "Session destroy"


@app.route("/")
def myIndex():
    myValue = 100

    # Looping
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    # conditioning
    # if A then Pass else Fail
    # if A then Excellent elif B then Good else Fail
    grade = "A"

    # set variable

    return render_template("index.html", myValue=myValue, days=days, grade=grade)


# routing to home
@app.route("/home")
def myHome():
    return render_template("home.html")


# routing to contact
@app.route("/contact")
def myContact():
    return render_template("contact.html")


# routing to about
@app.route("/about")
def myAbout():
    return render_template("about.html")


# routing with redirect
@app.route("/redirect-about")
def redirectAbout():
    return redirect(url_for("myAbout"))


# parsing integer value
@app.route("/parsing/<int:intval>")
def parsingInt(intval):
    return "Value is {}".format(intval)


# parsing string value
@app.route("/parsing/<string:stringval>")
def parsingString(stringval):
    return "Value is {}".format(stringval)


# argument parser
@app.route("/argument")
def parsingArgument():
    data = request.args.get("value")
    return "Value of the argument is {}".format(data)


if __name__ == "__main__":
    app.run(debug=True, port=8001)
