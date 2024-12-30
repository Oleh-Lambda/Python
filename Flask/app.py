# ------------------Flask------------------
# Це мікрофреймворк для Python, який дозволяє створювати веб-додатки.

# - Встановлення Flask -
# pip install flask

# 1. - Створення першого веб-додатку -
# import flask
# app = flask.Flask("Flask-app")
# @app.route("/")
# def home():
#     return "Hello, World!"
# if __name__ == "__main__":
#     app.run(debug=True)

# 2. - Передача параметрів в URL -
# import flask
# app = flask.Flask("Flask-app")
# @app.route("/")
# def home():
#     return "Welcome to my website!"
# @app.route("/<username>")
# def user_profile(username):
#     return f"Hello, {username}!"
# if __name__ == "__main__":
#     app.run(debug=True)

# 3. - Передача відповідних параметрів в URL -
# import flask
# app = flask.Flask("Flask-app")
# @app.route("/")
# def home():
#     return "Welcome to my website!"
# @app.route("/<int:number>")
# def number_test(number):
#     return f"Is {number}"
# if __name__ == "__main__":
#     app.run(debug=True)

# - методи flask -
# Flask() - створює об'єкт додатку, в параметрах - назва додатку.
# @app.route() - декоратор, який вказує, який URL викликає функцію.
# app.run(debug=True) - запускає сервер, в параметрах - включення режиму налагодження(дебаг).