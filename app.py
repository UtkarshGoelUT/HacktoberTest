from flask import Flask

app=Flask(__name__)

@app.route("/newfeature")
def new_feature():
    return "This route was added by Saksham Basandrai"

@app.route("/utkarsh")
def new_route():
	return "This is made by Utkarsh Goel"

@app.route("/")
def home():
	return "Hello Hacktoberfest!"

if __name__=='__main__':
	app.run(port=5500)
