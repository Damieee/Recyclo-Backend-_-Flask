# Recyclo

`Recyclo` is an innovative app that helps users recycle anything and everything. With its intuitive interface and robust recycling database, users can easily find information on how to properly dispose of various materials and items, including plastics, electronics, and household goods.  

<p align="center">
<img src="static/RECYCLO LOGO 1.png" alt="Recyclo logo 1" width="200"/>
<img src="static/RECYCLO LOGO 2.png" alt="Recyclo logo 2" width="200"/>
<img src="static/RECYCLO LOGO 3.png" alt="Recyclo logo 3" width="200"/>
<img src="static/RECYCLO LOGO 4.png" alt="Recyclo logo 4" width="200"/>
<img src="static/RECYCLO LOGO 5.png" alt="Recyclo logo 5" width="200"/>
<img src="static/RECYCLO LOGO 6.png" alt="Recyclo logo 6" width="200"/>
<img src="static/RECYCLO LOGO 7.png" alt="Recyclo logo 7" width="200"/>
<img src="static/RECYCLO LOGO 8.png" alt="Recyclo logo 8" width="200"/>
</p>

This Flask application provides API endpoints for `user authentication`, `password reset`, 1, and `recycling rewards`.

## Getting Started
Clone this repository
Install the required packages: `pip install -r requirements.txt`
To run the app, type `python app.py` in your terminal.

## Routes
- `POST /signup`: This route allows a new user to sign up by providing a username, email, password, and confirming the password. It creates a new user in the database and returns a success message.

- `POST /signin`: This route allows a user to sign in by providing their username or email and password. It returns a welcome message to the user if the provided credentials are correct.

- `POST /forgot_password`: This route allows a user to request a password reset email by providing their email address. It sends an email to the user containing a unique token that can be used to reset their password.

- `POST /reset_password`: This route allows a user to reset their password by providing their email address, the unique token that was sent to them via email, and a new password. If the email and token are valid, and the new password is confirmed, the user's password is reset.

- `GET /gps`: This route returns a list of recycling bins sorted by distance from the user's GPS location.

- `GET /rewards`: This route returns a list of available recycling rewards.

- `GET /rewards/:id`: This route returns details about a specific recycling reward identified by :id.

## Dependencies
- Flask
- Flask_SQLAlchemy
- Geopy
- Credits

## API LINK 

https://recyclo-v6gf.onrender.com/