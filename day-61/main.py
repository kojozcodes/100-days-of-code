from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = EmailField(
        label='Email',
        validators=[
            DataRequired(),
            Email(message='Invalid email'),
            Length(min=4, message='Enter a valid email address.')
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Enter a valid password.')
        ]
    )
    submit = SubmitField(label='Log in', validators=[DataRequired()])


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = 's3cr3tk3y'

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
