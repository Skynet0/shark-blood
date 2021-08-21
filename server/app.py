from flask import Flask, request, render_template

from chatbot import bot

app = Flask(__name__)
bot = bot()

@app.route("/")
def index():
    x = render_template("index.html")
    return x

@app.route("/chat", methods=["GET"])
def chat():
    data = request.args.get("data")
    if data:
        response, name = bot.response(data)
        response_obj = {'response' : response, 'name' : name}
    else:
        response_obj = {'response' : 'Please enter some text', 'name' : 'Nobody'}
    return response_obj

if __name__ == "__main__":
    app.run()