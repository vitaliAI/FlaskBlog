from flask import (
    Flask,
    render_template,
    url_for,
)

app = Flask(__name__)

posts = [
    {
        'author': 'Vitali Mueller',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 30, 2019',
    },
    {
        'author': 'Vitali Mueller',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 31 2019',
    },
    {
        'author': 'Vitali Mueller',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'Jan 1, 2020',
    }

]


@app.route('/')
def home():
    return render_template('home.html', posts=posts, title='Home Page')


@app.route("/about")
def about():
    return render_template('about.html', title='About Page')


if __name__ == '__main__':
    app.run(debug=True)
