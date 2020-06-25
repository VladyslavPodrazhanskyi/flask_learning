from flask import Flask, render_template, session


from .blueprints.test_methods.routes import test_methods_bp
from .blueprints.test_files.routes import files_bp
from .blueprints.valueables.routes import valueables
from .blueprints.html_test.routes import html_test
from .blueprints.request_test.routes import request_bp
from .blueprints.cookies.routes import cookies_bp
from .blueprints.redirect_and_errors.routes import redirect_and_errors_bp
# hw1
from .blueprints.hw1.Fruites.routes import fruites_bp
from .blueprints.hw1.Vegetables.routes import vegetables_bp
from .blueprints.hw1.Main.routes import main_hw1_bp



app = Flask(__name__)  # __name__ - переменная содержит имя главного модуля = 'flask_training'
print(__name__)

app.register_blueprint(valueables)
app.register_blueprint(html_test)
app.register_blueprint(test_methods_bp)
app.register_blueprint(files_bp)
app.register_blueprint(request_bp)
app.register_blueprint(cookies_bp)
app.register_blueprint(redirect_and_errors_bp)
# hw1
app.register_blueprint(fruites_bp)
app.register_blueprint(vegetables_bp)
app.register_blueprint(main_hw1_bp)



@app.errorhandler(404)
def error_404(e):
    return render_template('404.html', error=e), 404

@app.errorhandler(418)
def error_418(e):
    return render_template('error_418.html', error=e), 418

@app.errorhandler(501)
def error_501(e):
    return render_template('error_501.html', error=e), 501

# Session:

# Контекст запроса session представляет собой зашифрованную версию cookies
# хранит информацию от запроса к запросу ввиде словаря,
# для использования сессии обязательно нужно задать секретный ключ для приложения.

#generate secret key:
# import os
# print(os.urandom(16))

app.secret_key = b'wr\x15m\x04!\x88N!c\x01SP\xff\x13\xb7'

from datetime import timedelta

app.permanent_session_lifetime = timedelta(seconds=10)

@app.route('/test_session')
def test_session():
    session['name'] = 'Vlad'     # зашифрованную сессию, как и cookies
    session.permanent = True
    return 'Check your session'   # можно увидеть во вкладки application консоли разработчика в браузере.

# Можно расшифровать сессию в консоли браузера
# atob('eyJuYW1lIjoiVmxhZCJ9')
# "{"name":"Vlad"}"

# Logging - документирования состояния сервера, возникающих ошибок.

@app.route('/logging')
def log():
    app.logger.warning('This is warning')
    app.logger.error('This is error')
    app.logger.debug('This is debug')  # отображается только в режиме debug=True
    return 'We are testing logging!'


if __name__ == "__main__":
    app.run(debug=True)

# Замечание о сессиях на базе cookie:
# Flask возьмёт значения, которые вы помещаете в объект сессии,
# и сериализует их в cookie.
# Если вы обнаружили какие-либо значения,
# которые не сохраняются между запросами,
# а cookies реально включены, а никаких ясных сообщений об ошибках не было,
# проверьте размер cookie в ответах вашей страницы и сравните с размером,
# поддерживаемым веб-браузером.


# eyJuYW1lIjoiVmxhZCJ9.Xaw-ZQ.S8MTVDaL9xSddZ6B02YWA5u6tnc