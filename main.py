from flask import Flask, render_template, request,session,url_for,redirect,flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,DateTimeField,RadioField,SelectField,
                        TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] ='mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you ? : ',validators=[DataRequired()])
    neutured =BooleanField("Have you been neuteured ? : ")
    radio = RadioField("How is your mood? : ",
                        choices=[('happy','Happy'),
                        ('excited','Excited')])
    food_choice = SelectField(u'Pick your food : ',choices=[('chicken','Chicken'),('beef','Beef'),
    ('fs','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def mainpage():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutured'] = form.neutured.data    
        session['radio'] = form.radio.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        flash ('Data successfully submitted!!!')
        return redirect(url_for('thankyou'))
    return render_template('mainpage.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
