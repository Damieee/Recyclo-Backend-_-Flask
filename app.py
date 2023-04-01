from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import db, User, TokenBlacklist
from email_authentication import EmailAuthentication

app = FastAPI()

@app.on_event("startup")
async def startup():
    db.init_app(app)
    await db.create_all()

@app.post("/")
async def register(request: Request):
    data = await request.json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    email_authentication=EmailAuthentication(username=username, email=email)

    if not username or not email or not password:
        return JSONResponse(content={'message': 'Please enter all required information.'}, status_code=400)

    elif not email_authentication.validate_email_payload():
        return JSONResponse(content={'message': 'Please enter a valid username and email'}, status_code=400)


    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return JSONResponse(content={'message': 'That username or email already exists. Please choose another.'}, status_code=400)

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return JSONResponse(content={'message': f'User {username} successfully registered.'}, status_code=201)

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    username_or_email = data.get('username_or_email')
    password = data.get('password')

    if not username_or_email or not password:
        return JSONResponse(content={'message': 'Please enter your username or email and password.'}, status_code=400)

    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()

    if not user or not user.check_password(password):
        return JSONResponse(content={'message': 'Invalid login credentials. Please try again.'}, status_code=401)

    auth_token = user.encode_auth_token(user.id)
    return JSONResponse(content={'auth_token': auth_token.decode(), 'message': f'Welcome back, {user.username}.'}, status_code=200)

@app.post("/forgot-password")
async def forgot_password(request: Request):
    data = await request.json()
    email = data.get('email')

    if not email:
        return JSONResponse(content={'message': 'Please enter your email.'}, status_code=400)

    user = User.query.filter_by(email=email).first()

    if not user:
        return JSONResponse(content={'message': 'Invalid email. Please try again.'}, status_code=401)

    reset_token = user.generate_password_reset_token(email)

    # Here you would send an email to the user containing the reset token
    # You could use a service like SendGrid or Mailgun to handle this

    return JSONResponse(content={'message': 'An email containing instructions to reset your password has been sent.'}, status_code=200)

@app.post("/change-password")
async def change_password(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        resp = User.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp['sub']).first()
            data = await request.json()
            old_password = data.get('old_password')
            new_password = data.get('new_password')

            if not old_password or not new_password:
                return JSONResponse(content={'message': 'Please enter your old and newpasswords.'}, status_code=400)

        if not user.check_password(old_password):
            return JSONResponse(content={'message': 'Incorrect old password. Please try again.'}, status_code=401)

        user.set_password(new_password)
        db.session.commit()

        # Add token to blacklist to revoke user's previous tokens
        token = TokenBlacklist(token=auth_token)
        db.session.add(token)
        db.session.commit()

        return JSONResponse(content={'message': 'Password successfully changed.'}, status_code=200)

    else:
        return JSONResponse(content={'message': 'Authentication token is missing or invalid.'}, status_code=401)
