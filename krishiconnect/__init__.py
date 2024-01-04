from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from .forms import RegistrationForm, LoginForm, PriceForm, MarketplaceForm, GovForm, InventoryCategoryForm, InventoryCreateForm, CropCalendarForm
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
from .utils import weather_data
from .market import market_data
from flask_paginate import Pagination, get_page_parameter, get_page_args
from .Schemes import get_schemes_by_sector
from .program import get_data

state_choices = [['AD', 'Andhra Pradesh'], ['AR', 'Arunachal Pradesh'], ['AS', 'Assam'], ['BR', 'Bihar'], ['CG', 'Chattisgarh'], ['DL', 'Delhi'], ['GA', 'Goa'], ['GJ', 'Gujarat'], ['HR', 'Haryana'], ['HP', 'Himachal Pradesh'], ['JK', 'Jammu and Kashmir'], ['JH', 'Jharkhand'], ['KA', 'Karnataka'], ['KL', 'Kerala'], ['LD', 'Lakshadweep Islands'], ['MP', 'Madhya Pradesh'], ['MH', 'Maharashtra'], ['MN', 'Manipur'], ['ML', 'Meghalaya'], ['MZ', 'Mizoram'], ['NL', 'Nagaland'], ['OD', 'Odisha'], ['PY', 'Pondicherry'], ['PB', 'Punjab'], ['RJ', 'Rajasthan'], ['SK', 'Sikkim'], ['TN', 'Tamil Nadu'], ['TS', 'Telangana'], ['TR', 'Tripura'], ['UP', 'Uttar Pradesh'], ['UK', 'Uttarakhand'], ['WB', 'West Bengal']]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfasdfasdfasdlkfhasldkfh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from .models import User, Community, Harvest, Livestock

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('Login123.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(phone=form.phone.data).first():
            flash("A user has already been registered with this phone number!")
            return redirect(url_for('register'))
        user = User(name=form.name.data, phone=form.phone.data, pincode=form.pincode.data, state=form.state.data)
        db.session.add(user)
        db.session.commit()
        flash("You have been successfully registered!")
        return redirect(url_for('login'))
        #return 'helloads'
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Hola")
        user = User.query.filter_by(phone=form.phone.data).first()
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('dashboard'))
    else:
        print("Hi")
    return render_template('login.html', form=form)
    

@app.route('/check')
@login_required
def check():
    user = current_user
    return f"Hello you are logged in {user.name}"

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')

@app.route('/dashboard/weather')
@login_required
def weather():
    user = current_user
    data = weather_data(user.pincode)
    print(user, data)
    return render_template('weather.html', weather_data=data)
def get_prices(data, offset=0, per_page=10):
    return data[offset: offset + per_page]
    
@app.route('/dashboard/market', methods=['GET', 'POST'])
@login_required
def market():
    user = current_user
    user_state = request.args.get('state', default=user.state)
    
    for i in state_choices:
        if i[0]==user_state:
            user_state = i[1]
            break

    form = PriceForm()
    if form.validate_on_submit():
        state = form.state.data
        for i in state_choices:
            if i[0]==state:
                state = i[1]
                break
        return redirect(url_for('market', state = state))
    
    data = market_data(user_state)
    total = len(data)
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    pagination_users = get_prices(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, link_size=15, alignment='center')
    
    return render_template('market.html', market_data=pagination_users,page=page,per_page=per_page,
                           pagination=pagination, form=form)

@app.route('/marketplace/create', methods=['POST', 'GET'])
@login_required
def create():
    form = MarketplaceForm()
    if form.validate_on_submit():
        user = current_user
        item = Community(user_id=user.id, item=form.item.data, quantity=form.quantity.data, cost=form.cost.data)
        db.session.add(item)
        db.session.commit()
        return 'done'
    return render_template('marketsell.html', form = form)

@app.route('/marketplace')
def marketplace():
    data = Community.query.all()
    item = []
    for i in data:
        user = User.query.get(i.user_id)
        user_data = f"{user.name}, Contact: {user.phone}"
        item.append([user_data, i])
    return render_template('MarketPlace1.html',items=item, user=current_user)

@app.route('/schemes', methods=['POST', 'GET'])
def schemes():
    form = GovForm()
    if form.validate_on_submit():
        sector = form.sector.data
        return redirect(url_for('schemes', sector=sector))
    sector = request.args.get('sector', 'Agriculture')
    data = get_schemes_by_sector(sector)
    return render_template('SchemeGov.html', data=data, form=form)

@app.route('/inventory/add', methods=['POST', 'GET'])
@login_required
def inventory_add():
    category = request.args.get('category', 'Harvest')
    form = InventoryCreateForm()
    form2 = InventoryCategoryForm()
    if form2.validate_on_submit():
        category = form2.category.data
        return redirect(url_for('inventory_add', category=category))
    if form.validate_on_submit():
        if category == 'Harvest':
            item = Harvest(user_id=current_user.id, crop_name=form.name.data, quantity=form.quantity.data)
            db.session.add(item)
            db.session.commit()
        else:
            item = Livestock(user_id=current_user.id, livestock_name=form.name.data, quantity=form.quantity.data)
            db.session.add(item)
            db.session.commit()
        return redirect(url_for('inventory'))
    return render_template('inventorycreate.html', form=form, form2=form2, category=category)

@app.route('/inventory', methods=['POST', 'GET'])
@login_required
def inventory():
    category = request.args.get('category', 'Harvest')
    form = InventoryCategoryForm()
    if form.validate_on_submit():
        category = form.category.data
        return redirect(url_for('inventory', category=category))
    if category == 'Harvest':
        items = Harvest.query.filter_by(user_id=current_user.id).all()
    else:
        items = Livestock.query.filter_by(user_id=current_user.id).all()
    return render_template('inventory.html', form=form, items=items, category=category)

@app.route('/delete/<id>/<category>')
@login_required
def delete(id, category):
    if category == 'Harvest':
        item = Harvest.query.get(id)
    else:
        item = Livestock.query.get(id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('inventory'))
    else:
        return 'UNAUTHORIZED'
    
@app.route('/cropcalendar', methods=['POST', 'GET'])
def crop_calendar():
    form = CropCalendarForm()
    crop_id = request.args.get('crop_id', 0)
    if form.validate_on_submit():
        crop_id = form.crop.data
        return redirect(url_for('crop_calendar', crop_id = form.crop.data))
    data = get_data(int(crop_id))
    return render_template('Calendar.html', form=form, data=data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)