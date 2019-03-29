from flask import Flask
import logging, os

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
    UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)