#
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class blogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("write your own blog.",validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Add Comment')
# class SubscriptionForm(FlaskForm):
#    name = StringField('Name', validators = [Required()])
#    email = StringField('Email',validators=[Required(),Email()])
#    submit = SubmitField('submit')
#    def validate_email(self,data_field):
#        if Subscription.query.filter_by(email =data_field.data).first():
#            raise ValidationError('There is an account with that email')
#    def validate_name(self,data_field):
#        if Subscription.query.filter_by(name = data_field.data).first():
#            raise ValidationError('That name is taken')


class UpdateBlogForm(FlaskForm):
   title = StringField('Title', validators=[Required()])
   description = TextAreaField("write your own blog.",validators=[Required()])
   submit = SubmitField('Submit')