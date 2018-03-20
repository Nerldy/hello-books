from flask import Flask, render_template

app = Flask(__name__)


# user sign up
@app.route('/user/signup')
def user_sign_up():
	return render_template('user-sign-up.html', title='Sign Up')


# user sign in
@app.route("/user/signin")
def user_sign_in():
	return render_template('user-sign-in.html', title='Sign In')


if __name__ == '__main__':
	app.run(debug=1)
