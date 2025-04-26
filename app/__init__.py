from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__,
        template_folder=os.path.abspath("templates"),  
        static_folder=os.path.abspath("static")       
    )
    
    from .routes import bp
    app.register_blueprint(bp)
    
    return app