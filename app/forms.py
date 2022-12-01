from flask_wtf import FlaskForm

import wtforms as ws


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя',
                              validators=[ws.validators.DataRequired(), ws.validators.Length(min=5, max=15)])
    password = ws.PasswordField('Пароль',
                                validators=[ws.validators.DataRequired(), ws.validators.Length(min=8, max=20)])
    submit = ws.SubmitField('Зарегистрировать')


class EmployeeForm(FlaskForm):
    fullname = ws.StringField('ФИО сотрудника', validators=[ws.validators.DataRequired()])
    phone_number = ws.StringField('Номер телефона', validators=[ws.validators.DataRequired()])
    short_info = ws.TextAreaField('Коротка информация об сотруднике', validators=[ws.validators.DataRequired()])
    experience = ws.IntegerField('Опыт работы', validators=[ws.validators.DataRequired()])
    preferred_position = ws.StringField('Предпочитаемая позиция в компани')
    submit = ws.SubmitField('Сохранить')


    def validate_fullname(self, field):
        names_split = field.data.split(' ')
        if len(names_split) == 1:
            raise ws.ValidationError('ФИО не может состоять из одного символа')
        for name in names_split:
            if not name.isalpha():
                raise ws.ValidationError('ФИО не должно содержать спец символы и числы')
