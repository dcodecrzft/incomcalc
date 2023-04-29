from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def test():
    return "Hello world" #satvik dont change this for a sec #I did not change anything
        


if __name__ == "__main__":
    app.run(debug=True)