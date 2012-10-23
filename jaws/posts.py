from flask import Blueprint, render_template, abort
from jaws.models import Post

posts = Blueprint('posts', __name__,
                        template_folder='templates')

@posts.route('/posts')
def show_posts():
    posts = Post.query.all()

    return render_template('show_posts.html', posts=posts)


@posts.route('/post/<id>')
def show_post(id):
    post = Post.query.filter_by(id=id).first()

    return render_template('show_post.html', post=post)


@posts.route('/post/new')
def new_post():
    post = Post()

    return render_template('edit_post.html', post=post)
