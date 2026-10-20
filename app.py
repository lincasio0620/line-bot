from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE BOT OK"

@app.route("/callback", methods=["POST"])
def callback():

    print("=" * 50)
    print("收到 LINE 訊息")
    print(request.json)
    print("=" * 50)

    return "OK", 200

if __name__ == "__main__":
    app.run()