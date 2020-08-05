from flask import render_template, redirect, url_for
# import the app object from the ./application/__init__.py
from application import app, db
# define routes for / & /home, this function will be called when these are accessed
from application.models import Adding 
from application.forms import AddForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        postData = Adding(
            burnt = form.burnt.data,
            intake = form.intake.data,
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)
        
    
    return render_template('add.html', title='Caloric Intake', form=form)

@app.route('/remove', methods=['GET','POST'])
def remove():
    postData=Adding.query.all()

    return render_template('remove.html', title='Update or Remove', posts=postData)
