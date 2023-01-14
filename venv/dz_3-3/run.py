from flask import Flask, send_from_directory

# Импортируем блюпринты
from app.main.views import main_blueprint
from app.loader.views import loader_blueprint

# Создаем экземпляр Flask
app = Flask(__name__)

# регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# вьюшка для отдачи загруженных в /uploads файлов
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
