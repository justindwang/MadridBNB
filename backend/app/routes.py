from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import RequestButton


@app.route('/', methods=['GET', 'POST'])
@app.route('/req', methods=['GET', 'POST'])
def req():
    form = RequestButton()
    # if request.method=='POST':
    if form.validate_on_submit():
        flash('Hello from Server')
        print("Hello from Client")
    return render_template('req.html', title='Sign In', form=form)

