from flask import Flask
from routes import generator


app = Flask(__name__,static_url_path="/tmp",static_folder="tmp")

app.config.from_pyfile(config_file)

app.register_blueprint(generator)