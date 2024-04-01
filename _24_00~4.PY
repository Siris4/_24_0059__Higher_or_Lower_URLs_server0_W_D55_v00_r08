from flask import Flask
# import datetime as dt


app = Flask(__name__)


@app.route("/")
def hello_world():     #removed: now from return statement
    return f"""<h1>Guess a number between 0 and 9 </h1>  
    <img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW9xc3NoM2NjN3hxMzAzd20wd29pc3BtNzc1cmN6dDJtZGxjNTQxayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PK1YQhAoBOpP2/200.webp' width=400>"""

# remove below if unneeded:
if __name__ == "__main__":
    app.run(debug=True)   # can toggle this: True or False, depending on your needs
