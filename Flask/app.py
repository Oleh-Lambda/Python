# ------------------Flask------------------
# Це мікрофреймворк для Python, який дозволяє створювати веб-додатки.

# - Встановлення Flask -
# pip install flask

# - Створення першого веб-додатку -
import flask
app = flask.Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"
if __name__ == "__main__":
    app.run()