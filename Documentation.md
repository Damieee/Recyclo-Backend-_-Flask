# RECYCLO RESTful API

## Introduction:

This is a `RESTful API` that allows a mobile application to interact with a database of registered users, GPS data, recycle bin locations, and reward cards. It is built using Flask, a Python web framework that allows developers to create web applications and APIs quickly and easily.

## Endpoints:

- GET '/'
    This endpoint provides a welcome message to the user.

    Response: JSON object with the message "Welcome My Friend"

- GET/POST `/signup/<username>/<email>/<password>/<confirm_password>`
    This endpoint allows users to register with the application by providing their username, email, and password.

    Request Parameters:

    username: string
    email: string
    password: string
    Response:

    If successful, JSON object with the message "User <username> successfully registered." and HTTP status code 201 (Created)
    If unsuccessful, JSON object with an error message and HTTP status code 400 (Bad Request)

- GET/POST `/signin/string:username_or_email/<password>`
    This endpoint allows registered users to sign in by providing their username or email and password.

    Request Parameters:

    username_or_email: string
    password: string
    Response:

    If successful, JSON object with the message "Welcome back, <username>." and HTTP status code 200 (OK)
    If unsuccessful, JSON object with an error message and HTTP status code 401 (Unauthorized)

- GET/POST `/forgot_password/<email>`
    This endpoint allows users to initiate the password reset process by providing their email address.

    Request Parameters:

    email: string
    Response:

    If successful, JSON object with the message "An email containing instructions to reset your password has been sent." and HTTP status code 200 (OK)
    If unsuccessful, JSON object with an error message and HTTP status code 401 (Unauthorized)

- GET/POST `/reset_password/<token>/<new_password>/<confirm_password>`
    This endpoint allows users to reset their password by providing their email, token sent to them, new password, and confirm password.

    Request Parameters:

    email: string
    token: string
    new_password: string
    confrim_password: string
    Response:

    If successful, JSON object with the message "Password successfully changed." and HTTP status code 200 (OK)
    If unsuccessful, JSON object with an error message and HTTP status code 401 (Unauthorized)

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