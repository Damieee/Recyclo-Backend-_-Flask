
# RECYCLO RESTful API

## Introduction:

This is a `RESTful API` that allows a mobile application to interact with a database of registered users, GPS data, recycle bin locations, and reward cards. It is built using Flask, a Python web framework that allows developers to create web applications and APIs quickly and easily.

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


## Endpoints:

- GET `'/'`
    This endpoint provides a welcome message to the user.

    Response: JSON object with the message Welcome to Glidee API. Click <a href="https://github.com/Damieee/Recyclo/blob/main/Documentation.md">This Documentation</a> to learn more about the Routes end points.


- GET/POST `/signup`
  
    This endpoint allows users to register with the application by providing their username, email, and password.

    Create a new user
    
    parameters:
        - in: body
        - name: data
        - required:
            - email
            - first_name
            - last_name
            - password
            - password_confirm
        properties:
            - `email`:
                type: string
                description: This is the user's email address
            - `first_name`:
                type: string
                description: This is the user's first name
            - `last_name`:
                type: string
                description: This is the user's last name
            - `password`:
                type: string
                description: This is the user's password
            - `password_confirm`:
                type: string
                description: This is the user's password confirmation
    responses:
        - `201`:
            description: User registered successfully.
        - `400`:
            description: 
                - The passwords do not match.
                - User with email already exist.


- GET/POST `/signin`
    This endpoint allows registered users to sign in by providing their username or email and password.

    parameters:
        - in: body
        - name: data
        - required:
            - email
            - password
        properties:
            email:
                type: string
                description: This is the user's email address
            password:
                type: string
                description: This is the user's password
    responses:
        - `201`:
            description: User logged in successfully.
        - `400`:
            description: Invalid login credentials.
        - `500`:
            description: Error occured.
    """

- GET/POST `/forgot_password`
    This endpoint allows users to initiate the password reset process by providing their email address.

    Help users generate Token when they forget their Password
    ---
    parameters:
    -   in: body
        name: data
        required:
            - email
        properties:
            `email`:
                type: string
                description: This is the user's email address
    responses:
        - `200`:
            description: An email containing instructions to reset your password has been sent..
        - `400`:
            description: Invalid login credentials.


- GET/POST `/reset_password`
    This endpoint allows users to reset their password by providing their email, token sent to them, new password, and confirm password.

    Create a new password for users
    ---
    parameters:
    -   in: body
        name: data
        required:
            - email
            - token
            - new_password
            - confirm_password

        properties:
            - `email`:
                type: string
                description: This is the user's email address
            - `token`:
                type: string
                description: This is the token sent to the user's email address
            - `new_password`:
                type: string
                description: This is the user's new password
            - `confrim_password`:
                type: string
                description: This is the user's password confirmation
        responses:
            - `201`:
                description: Password successfully changed
            - `400`:
                description: 
                    - The passwords do not match
                    - This string can not be empty
                    - The passwords you entered do not match. Please make sure that both passwords are the same
            - `401`:
                description: 
                    - Invalid email. Please try again
                    - Invalid Token. Please try again


- GET `/gps`
    This endpoint retrieves the GPS coordinates of the user and returns a list of recycle bins sorted by their distance from the user.

    Request Parameters: None

    Response:

    If successful, JSON object with an array of bins sorted by their distance from the user and HTTP status code 200 (OK)
    If unsuccessful, JSON object with an error message and HTTP status code 404 (Not Found)

- GET `/rewards`
    This endpoint retrieves a list of reward cards that can be redeemed by the user.

    Request Parameters: None

    Response:

    If successful, JSON object with an array of reward cards and HTTP status code 200 (OK)

- GET `/rewards/int:reward_id`
    This endpoint retrieves a specific reward card by its ID.

    Request Parameters:

    reward_id: integer
    Response:

    If successful, JSON object with the reward card matching the provided ID and HTTP status code 200 (OK)
    If unsuccessful, JSON object with an error message and HTTP status code 404 (Not Found)

## Conclusion:

This API allows mobile developers to integrate the back-end functionality of the application into their front-end. By leveraging Flask and Python, the API provides authentication, GPS data, and rewards functionality to the application. Developers can use this documentation to understand the endpoints available and their input/output parameters.