
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

## GET `/`
    This endpoint provides a welcome message to the user.

    Response: JSON object with the message Welcome to Glidee API. Click <a href="https://github.com/Damieee/Recyclo/blob/main/Documentation.md">This Documentation</a> to learn more about the Routes end points.


## `/signup`

This endpoint allows users to register with the application by providing their username, email, and password.

### Create a new user

**HTTP Method**: `POST`

**Request Parameters:**

| Parameter | Type   | Required | Description                      |
|-----------|--------|----------|----------------------------------|
| `email`        | string | Yes      | The user's email address              |
| `first_name`   | string | Yes      | The user's first name                 |
| `last_name`    | string | Yes      | The user's last name                  |
| `password`     | string | Yes      | The user's password                   |
| `password_confirm` | string | Yes | The user's password confirmation |

**HTTP Response Codes:**

| Status Code | Description                       |
|-------------|-----------------------------------|
| `201`           | User registered successfully.             |
| `400`           | - The passwords do not match.<br/>- User with email already exists. |

## `/signin`

This endpoint allows registered users to sign in by providing their username or email and password.

**HTTP Method**: `POST`

**Request Parameters:**

| Parameter | Type   | Required | Description                          |
|-----------|--------|----------|--------------------------------------|
| `email`        | string | Yes      | The user's email address                  |
| `password`     | string | Yes      | The user's password                       |

**HTTP Response Codes:**

| Status Code | Description                       |
|-------------|-----------------------------------|
| `201`           | User logged in successfully.             |
| `400`           | Invalid login credentials.          |
| `500`           | Error occurred.                     |

## `/forgot_password`

This endpoint allows users to initiate the password reset process by providing their email address.

**HTTP Method**: `POST`

**Request Parameters:**

| Parameter | Type   | Required | Description                          |
|-----------|--------|----------|--------------------------------------|
| `email`        | string | Yes      | The user's email address                  |

**HTTP Response Codes:**

| Status Code | Description                       |
|-------------|-----------------------------------|
| `200`           | An email containing instructions to reset your password has been sent. |
| `400`           | Invalid login credentials.          |

## `/reset_password`

This endpoint allows users to reset their password by providing their email, token sent to them, new password, and confirm password.

**HTTP Method**: `POST`

**Request Parameters:**

| Parameter | Type   | Required | Description                          |
|-----------|--------|----------|--------------------------------------|
| `email`        | string | Yes      | The user's email address                  |
| `token`        | string | Yes      | The token sent to the user's email address |
| `new_password` | string | Yes      | The user's new password                  |
| `confirm_password` | string | Yes | The user's password confirmation |

**HTTP Response Codes:**

| Status Code | Description                       |
|-------------|-----------------------------------|
| `201`           | Password successfully changed.            |
| `400`           | - The passwords do not match.<br/>- This string cannot be empty.<br/>- The passwords you entered do not match. Please make sure that both passwords are the same. |
| `401`           | - Invalid email. Please try again.<br/>- Invalid token. Please try again. |


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