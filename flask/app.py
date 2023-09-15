from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ein-sehr-sicheres-geheimnis'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Für den Prototyp verwenden wir ein hardgecodetes 'User'-Objekt
users = {'mevemo': {'password': 'assword123', 'active': True}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.password = users[id]['password']

    def is_active(self):
        return users[self.id]['active']

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(form.username.data)
        if user and form.password.data == user.password:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Falscher Benutzername oder Passwort.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hallo, {current_user.id}! Willkommen im Dashboard.'

if __name__ == '__main__':
    app.run(debug=True)

