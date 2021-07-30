from flask import Flask
from flask import request, render_template, make_response, redirect

app=Flask(__name__)
app.config["SECRET_KEY"] = "ebl9am0t8he)h262kvi+1lrwm4*!4&41mu$gqwqcvz0xt5@g_p"

def create_resp_text(val:int) -> str:
    return f"<p class=\"num\">{val}</p>"

@app.route('/')
def index():
    cookie = request.cookies.get("count")
    if cookie:
        return render_template("test.html", cookie=create_resp_text(cookie))
    return render_template("test.html", cookie=create_resp_text(0))

@app.route('/click/')
def clicked():
    cookie = request.cookies.get("count")
    if cookie:
        cookie = int(cookie)
        cookie += 1
        resp = make_response(create_resp_text(cookie), 200)
        resp.set_cookie("count", str(cookie).encode(), samesite='Lax')
    else:
        resp = make_response(create_resp_text(1), 200)
        resp.set_cookie("count", "1".encode(), samesite='Lax')
    return resp

@app.route('/clear/')
def clear():
    resp = make_response(create_resp_text(0), 200)
    resp.set_cookie("count", str(0).encode(), samesite='Lax')
    return resp

@app.route('/impressum/')
def impressum():
    return render_template("impressum.html")