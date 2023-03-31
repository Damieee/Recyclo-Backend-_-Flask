from flask import request, jsonify
from models import User, db, app
from email_authentication import EmailAuthentication
import os



# Configure the Flask app to use a SQLite database using Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')

email_authentication=EmailAuthentication()


# Define the routes for the Flask app
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    email_authentication=EmailAuthentication(username=username, email=email)

    if not username or not email or not password:
        return jsonify({'message': 'Please enter all required information.'}), 400

    elif not email_authentication.validate_email_payload():
        return jsonify({'message': 'Please enter a valid username and email'}), 400


    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'That username or email already exists. Please choose another.'}), 400

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': f'User {username} successfully registered.'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username_or_email = data.get('username_or_email')
    password = data.get('password')

    if not username_or_email or not password:
        return jsonify({'message': 'Please enter your username or email and password.'}), 400

    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid login credentials. Please try again.'}), 401

    auth_token = user.encode_auth_token(user.id)
    return jsonify({'auth_token': auth_token.decode(), 'message': f'Welcome back, {user.username}.'}), 200

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Please enter your email.'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Invalid email. Please try again.'}), 401

    reset_token = user.generate_password_reset_token(email)

    # Here you would send an email to the user containing the reset token
    # You could use a service like SendGrid or Mailgun to handle this

    return jsonify({'message': 'An email containing instructions to reset your password has been sent.'}), 200

@app.route('/change-password', methods=['POST'])
def change_password():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if not auth_token:
        return jsonify({'message': 'Authentication token required.'}), 401

    data = request.get_json()
    current_password = data.get('current_password')
    new_password = data.get('new_password')

    if not current_password or not new_password:
        return jsonify({'message': 'Please enter your current password and new password.'}), 400

    resp = User.decode_auth_token(auth_token)

    if isinstance(resp, str):
        return jsonify({'message': resp}), 401

    user = User.query.filter_by(id=resp['sub']).first()

    if not user or not user.check_password(current_password):
        return jsonify({'message': 'Invalid current password. Please try again.'}), 401

    user.set_password(new_password)
    db.session.commit()

    return jsonify({'message': 'Password successfully updated.'}), 200


@app.route('/logout')
def logout():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            jti = resp['jti']
            token = TokenBlacklist(jti=jti, token=auth_token)
            try:
                # add the token to the blacklist
                db.session.add(token)
                db.session.commit()
                return jsonify({'message': 'Successfully logged out.'}), 200
            except Exception as e:
                return jsonify({'message': 'Something went wrong.', 'error': str(e)}), 500
        else:
            return jsonify({'message': resp}), 401
    else:
        return jsonify({'message': 'Authentication token required.'}), 401


@app.route('/profile')
def profile():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        resp = User.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp['sub']).first()
            return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

        else:
            return jsonify({'message': resp}), 401
        
    else:
        return jsonify({'message': 'Authentication token required.'}), 401



