from wtforms import Form,StringField

class CommentForm(Form):
    Word=StringField('Word')
    Time=StringField('Time')