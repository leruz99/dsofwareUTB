from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.documento import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
book_model = []


@app.route("/")
def index():
    return render_template('index.html') 


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')
    
@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)

@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)



@app.route('/books', methods=['GET'])
def books():
    return render_template('books.html')

@app.route('/books_detail', methods=['POST'])
def books_detail():
    id = request.form['id']
    title = request.form['title']
    category = request.form['category']
    n_pages = request.form['n_pages']
    author = request.form['author']
    pe = Document(id=id, title=title, category=category, n_pages=n_pages, author=author)
    book_model.append(pe)
    return render_template('books_detail.html', books_value=pe)

@app.route('/document')
def document():
    data1 = [(i.id, i.title, i.category, i.n_pages, i.author) for i in book_model]
    print(data1)
    return render_template('document.html', books_value=data1)










if __name__ == '__main__':
    app.run()