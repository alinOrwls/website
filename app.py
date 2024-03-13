from flask import Flask
from flask import render_template, request, redirect, session,url_for
from models import Book, Book_Datastore




app=Flask(__name__)
app.secret_key = "developer"

book_datastore = Book_Datastore()


@app.route('/')
def inicio():
        return render_template('site/index.html')


@app.route('/books')
def books():
        return render_template ('site/books.html', books=book_datastore.get_books())

@app.route('/books/show', methods=['POST'])
def books_show():
        name=request.form['txtName']
        url=request.form['txtURL']

        new_book = Book(name, url)
        book_datastore.add_instance(new_book)


        print(name)
        print(url)
        return render_template('books')

@app.route('/about')
def about():
        return render_template('site/about.html')

@app.route( '/admin' )
def admin_index():
        return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
        return render_template('admin/login.html')

#method to login in the admin user

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
        _user=request.form['txtUser']
        _password=request.form['txtPassword']
        print(_user)
        print(_password)

        if _user == "admin" and _password=="123":
                session[ "login "] = True
                session[ "user"] = "Manager"
                return redirect('/admin')

        return render_template("admin/login.html")

#log out and clear the session

@app.route('/singout')
def admin_sign_out():
        session.clear()
        return redirect('/admin/login')


@app.route('/admin/books')
def admin_books():
        return render_template('admin/books.html', books=book_datastore.get_books())



@app.route('/admin/books/save', methods=['POST'])
def admin_books_save():
        name=request.form['txtName']
        url=request.form['txtURL']

        new_book = Book(name, url)
        book_datastore.add_instance(new_book)


        print(name)
        print(url)
          

        return redirect(url_for("admin_books"))

#deleting the information in the table uinder admin/books

@app.route('/admin/books/delete', methods=['POST'])
def admin_books_delete():
         hash = request.form["hash"]
         book_datastore.delete_instance(hash)
         return redirect(url_for("admin_books"))
      

if __name__ == '__main__' :
            app.run(debug=True)