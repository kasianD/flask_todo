from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms.widgets import PasswordInput



class UserForm(FlaskForm):
	username = fields.StringField('Username', validators=[validators.input_required()])
	password = fields.StringField(
		'Password', widget=PasswordInput(hide_value=True), validators=[validators.input_required()]
		)


class TaskForm(FlaskForm):
	title = fields.StringField('Title', validators=[validators.input_required()])
	description = fields.StringField('Description', validators=[validators.input_required()])
	due_date = fields.DateTimeField('Due date', format='%Y-%m-%dT%H:%M', validators=[validators.input_required()])
	is_accomplished = fields.BooleanField('Finish taks')
