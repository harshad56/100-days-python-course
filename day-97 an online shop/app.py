from flask import Flask, render_template, redirect, url_for, flash

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SubmitField

from wtforms.validators import DataRequired

import stripe


app = Flask(__name__)

# Replace with a secure secret key
app.config['SECRET_KEY'] = 'your_secret_key'


# Replace with your Stripe API keys

stripe.api_key = 'your_stripe_secret_key'


# Sample products

products = [

    {"id": 1, "name": "Product 1", "price": 10.0},

    {"id": 2, "name": "Product 2", "price": 15.0},

    {"id": 3, "name": "Product 3", "price": 20.0},

]


class PurchaseForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired()])

    product_id = IntegerField('Product ID', validators=[DataRequired()])

    submit = SubmitField('Purchase')


@app.route('/')
def index():

    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:

        return redirect(url_for('index'))

    form = PurchaseForm()

    if form.validate_on_submit():

        # Charge the user using Stripe

        try:

            customer = stripe.Customer.create(
                email=form.email.data, name=form.name.data)

            charge = stripe.Charge.create(

                customer=customer.id,

                amount=int(product["price"] * 100),  # Convert to cents

                currency='usd',

                description=f'Purchase of {product["name"]}'

            )

            flash('Purchase successful!', 'success')

            return redirect(url_for('index'))

        except stripe.error.CardError as e:

            flash(f'Error: {e.error.message}', 'danger')

    return render_template('product.html', product=product, form=form)


if __name__ == '__main__':

    app.run(debug=True)
