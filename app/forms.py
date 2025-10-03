from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(max=200)])
    author = StringField('Автор', validators=[Optional(), Length(max=100)])
    body = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class CommentForm(FlaskForm):
    author = StringField('Автор', validators=[Optional(), Length(max=100)])
    body = TextAreaField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Добавить')
