from flask import Flask
from app.routes import main

def create_app():
    app = Flask(
        __name__,
        template_folder="app/templates",  
        static_folder="app/static"  
    )
    app.register_blueprint(main)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
