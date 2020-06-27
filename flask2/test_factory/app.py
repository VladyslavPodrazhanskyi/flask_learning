from flask import Flask
from main import main
from config import run_config

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x89p\xc9"@j\xb9\xeb\xcd\\\x9e\xc4\xf7\xfe<T'

app.config.from_object(run_config())

app.register_blueprint(main)


if __name__ == '__main__':
    app.run()
