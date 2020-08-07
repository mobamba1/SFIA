from flask import render_template, redirect, url_for
# import the app object from the ./application/__init__.py
from application import app, db
# define routes for / & /home, this function will be called when these are accessed
from application.models import Adding, User 
from application.forms import AddForm, UpdateAddForm

@app.route('/')
@app.route('/home')
def home():
        
    John = User(name='John')
    db.session.add(John)
    db.session.commit()
        
    return render_template('home.html', title='Home')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        postData = Adding(
            burnt = form.burnt.data,
            intake = form.intake.data,
            owner_id = 1,            
            
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
    form = UpdateAddForm()
    if form.validate_on_submit():
        number = form.calorie_id.data
        update = Adding.query.filter_by(id=number).first()
        update.burnt = form.burnt.data
        update.intake = form.intake.data
        db.session.commit()
        return redirect(url_for('remove'))

    return render_template('remove.html', title='Update or Remove', posts=postData, form=form)

@app.route('/remove/delete', methods=['GET', 'POST'])
def remove_delete():
    update_this = db.session.query(Adding).delete()
    db.session.commit()
    return redirect(url_for('remove'))


