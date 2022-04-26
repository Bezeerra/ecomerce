from venv import create
from flask import Flask, session
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

#ligacao com o banco de dados
engine = create_engine("mysql+pymysql://")


app = Flask(__name__)

#admin =  'tema'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
#app.config SQLALCHEMY
Bootstrap(app) #css na pagina
admin = Admin()

#colocado em função para chamar nas configs
def init_app(app):
    admin.name= "CodeFoods"
    #ler a biblioteca bootstrap em serverPython
    admin.template_mode ="bootstrap3" #aceita o 2 também
    #admin.add_view(ModelView(User, db.session))
    #admin.add_view(ModelView(Post, db.session))
    admin.init_app(app)
    

if __name__ == "__main__":
    app.run(debug=True)