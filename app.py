from flask import Flask, render_template, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap
from collections import OrderedDict
from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import InputRequired
import choice
import table


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This will be hard to guess'
bootstrap = Bootstrap(app)
grp_one = choice.grps_one
grp_two = choice.grps_two


class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class CategoryForm(FlaskForm):
    budget_amount = DecimalField('Enter Budget Amount: ', validators=[InputRequired()])
    cat_one = MultipleCheckboxField('Select your Items', choices=grp_one, coerce=str)
    cat_two = MultipleCheckboxField('Select your Items', choices=grp_two, coerce=str)
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CategoryForm()
    if form.validate_on_submit():
        session['total_budget'] = float(form.budget_amount.data)
        session['category'] = form.cat_one.data + form.cat_two.data
        choice.total_budget = float(session['total_budget'])
        session['service_provider'] = choice.choose_providers(choice.cat_groups, session['category'],
                                                              choice.total_budget)[1]
        session['message'] = choice.choose_providers(choice.cat_groups, session['category'], choice.total_budget)[0]
        print(session['total_budget'], session['category'], session['service_provider'], session['message'])
        return redirect(url_for('display'))
    name = None
    known = None
    return render_template('index.html', form=form, name=name, known=known, grp_one=grp_one)


@app.route('/display', methods=['GET'])
def display():
    budget = session.get('total_budget')
    items = choice.item_distro(choice.cat_groups, session.get('category'))
    distributors = session.get('service_provider')
    msg = session.get('message')
    dealers = table.populate_table()
    dealers_list = ['cake', 'photography', 'venues', 'florists', 'bands', 'caterers']
    return render_template('display.html', budget=budget, items=items, distributors=distributors,
                           msg=msg, dealers=dealers, dealers_list=dealers_list)



