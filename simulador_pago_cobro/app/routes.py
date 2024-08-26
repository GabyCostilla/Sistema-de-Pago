from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User, Product, Order, Payment
from .forms import LoginForm, RegistrationForm, ProductForm, OrderForm, PaymentForm
from . import create_app

app = create_app()

@app.route('/')
@login_required
def home():
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data)
        db.session.add(product)
        db.session.commit()
        flash('Product has been created!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_product.html', form=form)

@app.route('/order/new', methods=['GET', 'POST'])
@login_required
def new_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(user_id=current_user.id, total_amount=form.total_amount.data)
        db.session.add(order)
        db.session.commit()
        flash('Order has been created!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_order.html', form=form)

@app.route('/payment/new', methods=['GET', 'POST'])
@login_required
def new_payment():
    form = PaymentForm()
    if form.validate_on_submit():
        payment = Payment(order_id=form.order_id.data, amount=form.amount.data)
        db.session.add(payment)
        db.session.commit()
        flash('Payment has been processed!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_payment.html', form=form)
