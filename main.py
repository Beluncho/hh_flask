from flask import Flask, render_template, request
from hh_requests_Fl import parce

app = Flask(__name__)


@app.get('/index')
@app.get("/")
def index():
    return render_template('index.html')


@app.route("/form/")
def form():
    return render_template('form.html')


@app.route("/contacts/")
def contacts():
    return render_template('contacts.html')


@app.post('/result/')
def result():
    """
    Вывод результата обработки запроса
    :return: страница с результатами
    """
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}  # data | vac - в Python 3.10 можно сделать так
    print(dat)
    return render_template('about.html', res=dat)


if __name__ == "__main__":
    app.run(debug=True)