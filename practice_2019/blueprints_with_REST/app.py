# Основное приложение

from flask import Flask

# Импорт блупринтов.
from main import main_blueprint # Импорт блупринта
from vegetables import vegetables_bp
from fruites import fruites_bp
from fish import fish_bp



app = Flask(__name__)




# регистрация блупринтов.
app.register_blueprint(main_blueprint)
app.register_blueprint(vegetables_bp)
app.register_blueprint(fruites_bp)
app.register_blueprint(fish_bp)


if __name__ == '__main__':
    app.run(debug=True)

