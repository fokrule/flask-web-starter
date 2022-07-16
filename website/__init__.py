from flask import Flask

def create_app(): #created a function named as create_app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsjhnsljskls shs'

    #import blueprint
    from .views import views # first .views is the file name and last views is the blueprint name
    from .auth import auth

    #register blueprint 
    app.register_blueprint(views, url_prefix='/') # this will be the prfix after base url and before route
    app.register_blueprint(auth, url_prefix='/')
    return app
