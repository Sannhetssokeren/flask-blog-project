from flask import Flask, render_template

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

# Определяем маршрут для главной страницы ('/')
@app.route('/')
def blog():
    """
    Отображает страницу блога.
    """
    # Рендерим HTML-шаблон 'blog.html'
    return render_template('blog.html')

# Проверяем, что скрипт запущен напрямую (а не импортирован)
if __name__ == '__main__':
    # Запускаем веб-сервер Flask в режиме отладки (debug=True)
    # Внимание: debug=True не следует использовать в продакшене!
    app.run(debug=True)