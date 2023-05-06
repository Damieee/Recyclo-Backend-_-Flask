from flask import request, jsonify, abort, render_template
from models import db, User
from flask_swagger import swagger
from Flask_Cors import CORS
from sqlalchemy.exc import IntegrityError
from webargs.flaskparser import use_args
from webargs import fields
from authentication.email_authentication import EmailAuthentication
from geopy.distance import geodesic
from GPS_Tracking.recycle_bin_locations import bins, Gps
from reward.recycle_reward import reward_cards
from send_token import Token
from flask import Flask



# Initialize the Flask application
app = Flask(__name__)

# Cross Origin Resource sharing to allow Javascript frontend code access Web Server
CORS(app, origins=['http://localhost:5000, http://localhost'])

# Configure the Flask app to use a SQLite database using Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
gps=Gps()
token=Token()
new_token=token.confirm_token()

# Define the routes for the Flask app
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# User Signup Route
@app.post('/signup')

@use_args({
    'first_name': fields.Str(required=True, error_messages={'required': 'The first_name field is required'}),
    'last_name': fields.Str(required=True, error_messages={'required': 'The last_name field is required'}),
    'email': fields.Email(required=True, error_messages={'required': 'The email field is required'}),
    'password': fields.Str(required=True, error_messages={'required': 'The password field is required'}),
    'password_confirm': fields.Str(required=True, error_messages={'required': 'The password confirmation field is required'})
}, location='json')

def signup(data):
    if data['password'] != data['password_confirm']:
        return jsonify({'message': 'The passwords do not match.'}), 400

    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    user.set_password(data['password'])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User with email already exist.'}), 400

    return jsonify({'message': f'User registered successfully.'}), 201

# User signin Route
@app.post('/login')

@use_args({
    'email': fields.Email(required=True),
    'password': fields.Str(required=True),
}, location='json')

def signin(data):

    user = (
        db.session
        .query(User)
        .filter((User.email == data['email']))
        .first()
    )
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid login credentials.'}), 400

    try:
        auth_token = user.generate_auth_token(user.id)
    except Exception:
        return jsonify({'message': 'Error occured.'}), 500

    return jsonify({
        'message': 'User logged in successfully.',
        'data': {'token': auth_token}
    }), 200

# Forgot email route
@app.route('/forgot_password/<email>', methods=['GET','POST'])

@use_args({
    'email': fields.Email(required=True, error_messages={'required': 'The email field is required'})
}, location='json')

def forgot_password(data):

    email= data['email']

    if not email:
        return jsonify({'message': 'Invalid login credentials.'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid email. Please try again.'}), 400

    reset_token = token.send_token(email=email)
    

    # Here you would send an email to the user containing the reset token
    # I plan to update this code later by using a service like SendGrid or Mailgun to handle this

    return jsonify({'message': 'An email containing instructions to reset your password has been sent.'}), 200

# Reset password route
@app.route('/reset_password', methods=['GET', 'POST'])

@use_args({
    'email': fields.Str(required=True, error_messages={'required': 'The first_name field is required'}),
    'token': fields.Str(required=True, error_messages={'required': 'The last_name field is required'}),
    'new_password': fields.Str(required=True, error_messages={'required': 'The password field is required'}),
    'confrim_password': fields.Str(required=True, error_messages={'required': 'The password confirmation field is required'})
}, location='json')

def reset_password(data):

    email = data['email']
    token = data['token']
    new_password = data['new_password']
    confirm_password = data['confirm_password']

    if not email:
        return jsonify({'message': 'This string can not be empty'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid email. Please try again.'}), 401

    if token != new_token:
        return jsonify({'message': 'Invalid Token. Please try again.'}), 401

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid email. Please try again.'}), 401

    if not new_password:
        return jsonify({'message': 'This string cannot be empty'}), 400

    if new_password != confirm_password:
        return jsonify({'message': 'The passwords you entered do not match. Please make sure that both passwords are the same.'}), 400


    user.set_password(new_password)
    db.session.commit()

    return jsonify({'message': 'Password successfully changed.'}), 200


@app.route('/gps')
def get_bins():
    location=gps.gps_location()
    user_lat = location["Latitude"]
    user_lon = location["Latitude"]

    bins_with_distance = [
        {
            'id': bin['id'],
            'name': bin['name'],
            'address': bin['address'],
            'distance': geodesic((user_lat, user_lon), (bin['lat'], bin['lon'])).km
        }
        for bin in bins
    ]
    bins_sorted_by_distance = sorted(bins_with_distance, key=lambda bin: bin['distance'])
    return jsonify({'bins': bins_sorted_by_distance})

@app.route('/rewards', methods=['GET'])
def get_rewards():
    return jsonify({'rewards': reward_cards})

@app.route('/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    reward = [reward for reward in reward_cards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    return jsonify({'reward': reward[0]})

@app.get('/spec')
def spec():
    swag = swagger(app)
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'Glidee App API'
    return jsonify(swag)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
