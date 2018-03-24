from flask import Flask

app = Flask(__name__)

# dummy books
books = [
	{
		"bookTitle": "Dummy Book Title",
		"bookSynopsis": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
		"bookAuthor": ["John Doe", "Jane Doe", "O.D. Doe"],
		"isbn": "12345a9bcde"
	}
]


# GET /api/books - Retrieves all books
@app.route('/api/v1/books')
def get_all_books():
	"""Retrieves all books"""
	pass


# GET /api/books/<bookId> - Get a book
@app.route('/api/books/v1/<bookid>')
def get_book(bookid):
	"""Retrieves one book through it's Id"""
	pass


# POST /api/books - Add a book
@app.route('/api/v1/books', methods=['POST'])
def create_book():
	"""Adds a book to the database"""
	pass


# POST /api/users/books/<bookId> - Borrow a book
@app.route('/api/v1/users/books/<bookid>', methods=['POST'])
def create_user_book(bookid):
	"""Creates user book"""
	pass


# TODO: DELETE /api/books/<bookid> - Remove a book
# TODO: PUT /api/books/<bookId> - Modify a book's information
# TODO: POST /api/auth/register - Creates a user account
# TODO: POST /api/auth/login - Logs in user
# TODO: POST /api/auth/logout - Logs out user
# TODO: POST /api/auth/reset-password - Password reset


app.run(port=5000)
