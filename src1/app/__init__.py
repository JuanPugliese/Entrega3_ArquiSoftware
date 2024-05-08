from flask import Flask 
from .controller import tasks_bp

app = Flask( __name__)
app.register_blueprint(tasks_bp)
if __name __== '__main__':
    app.run (debug=True)