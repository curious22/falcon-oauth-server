# /v1/users

__Allowed methods__: GET, POST

__Title__: Endpoint for working with users

***

__Title__: Create a new user

__URL__: /v1/users/ 

__Method__: HTTP POST

__Content-Type__: application/json

__URL Params__: 
- username=[string] * (min: 4, max: 20), 
- email=[string] * (max: 320, [a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}), 
- password=[string] * (min: 8, max 64, [0-9a-zA-Z]\w{3,14})

__Success Response__:
- Status: 200 OK
- Code: 200
- Description: User successfully created
- Content:
    ```json
    {
      "meta": {
        "code": 200,
        "message": "OK"
      },
      "data": null
    }
    ```

__Error Response__:
- Status: 400 Bad Request
- Code: 20 
- Description: User with this email already exists
- Content:
    ```json
    {
      "meta": {
        "code": 20,
        "message": "User with this email already exists"
      }
    }
    ```

***

__Title__: Return a list of existing users

__URL__: /v1/users/ 

__Method__: HTTP GET

__Success Response__:
- Status: 200 OK
- Code: 200
- Description: Rerurn a list of existing users
- Content:
```json
{
  "meta": {
    "code": 200,
    "message": "OK"
  },
  "data": [
    {
      "email": "test1@gmail.com",
      "username": "test1"
    },
    {
      "email": "te2st1@gmail.com",
      "username": "213123"
    },
    {
      "email": "te2st231@gmail.com",
      "username": "213123"
    }
  ]
}
```