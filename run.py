from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from app import app
from app import admin
#dynaconf
#flask_admin
#SQLAlchemy
#flask_simplelogin
#flask_sqlalchemy




#**locals()
@app.route('/')
def index():
    params = ['Matheus', 'Bezerra']
    return render_template("index.html", products=params)

if __name__ == "__main__":
    app.run(debug=True)