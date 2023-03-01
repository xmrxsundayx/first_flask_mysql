from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend

app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)


@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)