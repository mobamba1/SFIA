from flask import render_template, redirect, url_for
# import the app object from the ./application/__init__.py
from application import app, db
# define routes for / & /home, this function will be called when these are accessed
from application.models import Adding, User 
from application.forms import AddForm, UpdateAddForm

@app.route('/')
@app.route('/home')#name of the page when trying to acces through HTTP
def home():#name of page
        
    John = User(name='John')#create new user 
    db.session.add(John)
    db.session.commit()
        
    return render_template('home.html', title='Home')#renteders the html.page


@app.route('/add', methods=['GET', 'POST'])#gets data or post data
def add():
    form = AddForm()# creates a instance of form so that it can take in data to be added to SQL
    if form.validate_on_submit():#only triggers when clicked on submit button
        postData = Adding(#these are the data taken from forms 
            burnt = form.burnt.data,
            intake = form.intake.data,
            owner_id = 1,            
            
        )

        db.session.add(postData)#adds data to SQL
        db.session.commit()#sends any data included

        return redirect(url_for('home'))#returns user back to home

    else:
        print(form.errors)#prints any erros it encounters
        
    
    return render_template('add.html', title='Caloric Intake', form=form)

@app.route('/remove', methods=['GET','POST'])
def remove():
    postData=Adding.query.all()#prints all data in from SQL
    form = UpdateAddForm()
    if form.validate_on_submit():
        number = form.calorie_id.data#
        update = Adding.query.filter_by(id=number).first()#using the id user input we can identify in the sql which needs to updated
        update.burnt = form.burnt.data
        update.intake = form.intake.data
        db.session.commit()
        return redirect(url_for('remove'))

    return render_template('remove.html', title='Update or Remove', posts=postData, form=form)

@app.route('/remove/delete', methods=['GET', 'POST'])
def remove_delete():
    update_this = db.session.query(Adding).delete()#delets everything inside Adding
    db.session.commit()
    return redirect(url_for('remove'))


