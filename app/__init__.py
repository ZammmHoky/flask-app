from flask import Flask

def create_app():
  
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '454c0496e82349572c0fd8a4d1dfcafa7acf4ad9b8bd49ae'  
    
    from .routes import main
    app.register_blueprint(main)

    return app
