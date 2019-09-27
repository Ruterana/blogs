#
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class blogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("write your own blog.",validators=[Required()])
	# category = RadioField('Label', choices =[ ('love','love'),('product','product'),('motivation','motivation')],validators=[Required()])
	submit = SubmitField('Submit')
