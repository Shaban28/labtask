from flask import Flask

app = Flask(__name__)  # Corrected version

@app.route("/")
def home():
    return "hello,Shaban"

if __name__ == "__main__":
    app.run()
