# AnchiBackend

Backend for Anchi - A project for my school homework.

<br>

---

<br>

## API List

Click the name of api to read more details.

| Name                                | Method | Path                |
| ----------------------------------- | ------ | ------------------- |
| [Register](#register-api)           | `POST` | `/user/`            |
| [Login](#login-api)                 | `POST` | `/login/`           |
| [Logout](#logout)                   | `POST` | `/logout/`          |
| [All Foods](#all-foods)             | `GET`  | `/all-foods/`       |
| [Favourite Foods](#favourite-foods) | `GET`  | `/favourite-foods/` |

<br>

---

<br>

## Register API

<br>

> Register a new User.

<br>

- Request example:

  ```json
  { "username": "Minh Huong", "password": "minhehe123" }
  ```

- Response example:

  ```json
  {
    "username": "Minh Huong",
    "token": "b48d7ff8fd3de7417c451156a7516fc75aecf40d"
  }
  ```

<br>

[^](#api-list)

---

<br>

## Login API

<br>

> Log in as an User.

<br>

- Request example:

  ```json
  { "username": "Minh Huong", "password": "minhehe123" }
  ```

- _Login Successful_ Response example:

  ```json
  {
    "username": "Minh Huong",
    "token": "b48d7ff8fd3de7417c451156a7516fc75aecf40d"
  }
  ```

- _Login Failed_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#api-list)

---

## Logout

> Log out

<br>

- Request body can be null. Only need the token.

- _Logout Successful_ Response example:

  ```json
  { "detail": "Log out successfully." }
  ```

<br>

[^](#api-list)

---

## All Foods

> Get a list of all of the foods from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "banh mi",
      "description": "banh mi bnh mi banh mi banh mi",
      "address": "ai ma biet duoc",
      "recipe": "banh mi",
      "tags": [],
      "ingredients": []
    },
    {
      "id": 2,
      "name": "banh mi 2",
      "description": "banh mi banh mi banh mi",
      "address": "banh mi",
      "recipe": "banh mi",
      "tags": [],
      "ingredients": []
    }
  ]
  ```

<br>

[^](#api-list)

---

## Favourite Foods

> Get a list of user's favourite foods

<br>

- Response example:

```json
{
  "username": "user003",
  "favouriteFood": [
    {
      "id": 1,
      "name": "banh mi",
      "description": "banh mi bnh mi banh mi banh mi",
      "address": "ai ma biet duoc",
      "recipe": "banh mi",
      "tags": [],
      "ingredients": []
    }
  ]
}
```

- _Anonymous User_ Response:

```json
{
  "detail": "You must sign in to have your favourite foods listed."
}
```

<br>

[^](#api-list)

---
