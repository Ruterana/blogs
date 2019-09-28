#
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class blogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("write your own blog.",validators=[Required()])
	submit = SubmitField('Submit')


class commentForm(FlaskForm):
	
	description = TextAreaField("leave comment.",validators=[Required()])
	submit = SubmitField('Add comment')