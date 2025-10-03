from datetime import datetime
from . import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    comments = db.relationship(
        'Comment',
        back_populates='post',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )

    def __repr__(self):
        return f"<Post {self.id} {self.title!r}>"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    author = db.Column(db.String(100))
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship('Post', back_populates='comments')

    def __repr__(self):
        return f"<Comment {self.id} post={self.post_id}>"