from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#dynaconf
#flask_admin
#SQLAlchemy
#flask_simplelogin
#flask_sqlalchemy


app = Flask(__name__)
Bootstrap(app)


#**locals()
@app.route("/")
def index():
    products = ['ciabatta', 'baguete', 'Pretzel']
    return render_template("index.html", products=products)



if __name__ == "__main__":
    app.run(debug=True)