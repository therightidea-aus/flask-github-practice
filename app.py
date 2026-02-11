from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello GitHub + Flask 👋, we hope you have a good night"

if __name__ == "__main__":
    app.run(debug=True)
