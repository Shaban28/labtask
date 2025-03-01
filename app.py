from flask import Flask

app = Flask(__name__)  # Corrected version

@app.route("/")
def home():
    return "hello,Shaban Qadeer Khan"

if __name__ == "__main__":
    app.run()
