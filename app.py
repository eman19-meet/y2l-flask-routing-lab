from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/SHOP')
def shop_page():
	stuff = ["stuff", "stuff", "stuff"]
	return render_template("shop.html", stuff=stuff)

if __name__ == '__main__':
   app.run(debug = True)