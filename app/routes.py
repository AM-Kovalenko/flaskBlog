from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Post, Comment
from .forms import PostForm, CommentForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@bp.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=form.author.data)
        db.session.add(post)
        db.session.commit()
        flash('Пост создан', 'success')
        return redirect(url_for('main.index'))
    return render_template('post_form.html', form=form, title='Новый пост')

@bp.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    return render_template('post.html', post=post, form=form)

@bp.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_id=post.id, author=form.author.data, body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий добавлен', 'success')
    else:
        flash('Ошибка при добавлении комментария', 'danger')
    return redirect(url_for('main.view_post', post_id=post.id))

@bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.body = form.body.data
        db.session.commit()
        flash('Пост обновлён', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    return render_template('post_form.html', form=form, title='Редактировать пост')

@bp.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Пост удалён', 'success')
    return redirect(url_for('main.index'))
