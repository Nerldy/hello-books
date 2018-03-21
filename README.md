# HELLO BOOKS APP

Hello-Books is a simple application that helps manage a library and its processes like stocking, tracking and renting books. With this application users are able to find and rent books. The application also has an admin section where the admin can do things like add books, delete books, increase the quantity of a book etc.

## Run App

To run the app, on the terminal

```
export FLASK_APP=hello_books.py
export FLASK_DEBUG=1
flask run
```

On your browser, go to ***localhost:5000***

Available urls right now are:
- 
* __user/signin__
* __user/signup__
* __user/home__
* __admin/home__
* __admin/search/notreturned__
* __admin/admin/search/userborrowed__
