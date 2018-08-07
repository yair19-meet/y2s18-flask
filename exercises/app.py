from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", players = ["Derrick Rose", "Stephen curry", "Lebron James", "Kevin Durant"], likes_same_sport=False)

if __name__ == '__main__':
   app.run(debug = True)