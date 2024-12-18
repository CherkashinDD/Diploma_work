from flask import Blueprint, render_template, flash
from forms import UserRegister
from db_cherepaha import db, User



user_registration_routes = Blueprint('user_registration', __name__)


@user_registration_routes.route("/user_registration", methods=['GET', 'POST'])
def user_registration():
    form = UserRegister()
    if form.validate_on_submit():
        user = User.query.filter_by(
            last_name=form.last_name.data,
            first_name=form.first_name.data,
            patronymic=form.patronymic.data
        ).first()
        if user:
            flash('Такой пользователь уже существует', 'error')
        elif form.password.data != form.confirm_password.data:
            flash('Пароли не совпадают', 'error')
        else:
            new_user = User(
                last_name=form.last_name.data,
                first_name=form.first_name.data,
                patronymic=form.patronymic.data,
                phone_number=form.phone_number.data,
                email=form.email.data
            )
            db.session.add(new_user)
            db.session.commit()
            flash(
                f'{form.last_name.data} {form.first_name.data} {form.patronymic.data} успешно зарегистрировался(лась)', 'success')
    return render_template('user_registration.html', form=form)
