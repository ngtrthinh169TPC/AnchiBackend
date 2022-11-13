# AnchiBackend

Backend for Anchi - A project for my school homework.

This project is currently (2022) being deployed [here](https://anchi-api.aqaurius6666.space/).

<br>

---

<br>

## API List

Click the name of API for more details.

### User APIs

| Name                      | Method | Path       |
| ------------------------- | ------ | ---------- |
| [Register](#register-api) | `POST` | `/user/`   |
| [Login](#login-api)       | `POST` | `/login/`  |
| [Logout](#logout)         | `POST` | `/logout/` |

<br>

### Food APIs

| Name                                        | Method | Path                |
| ------------------------------------------- | ------ | ------------------- |
| [All Foods](#all-foods)                     | `GET`  | `/all-foods/`       |
| [Favourite Foods](#favourite-foods)         | `GET`  | `/favourite-foods/` |
| [POST Favourite Food](#post-favourite-food) | `POST` | `/favourite-foods/` |
| [Blacklist Foods](#blacklist-foods)         | `GET`  | `/blacklist-foods/` |
| [POST Blacklist Food](#post-blacklist-food) | `POST` | `/blacklist-foods/` |
| [Next Food](#next-food)                     | `GET`  | `/next-food/`       |
| [POST Food](#post-food)                     | `POST` | `/food/`            |

<br>

### Restaurant APIs

| Name                                                    | Method | Path                      |
| ------------------------------------------------------- | ------ | ------------------------- |
| [All Restaurants](#all-restaurants)                     | `GET`  | `/all-restaurants/`       |
| [Favourite Restaurants](#favourite-restaurants)         | `GET`  | `/favourite-restaurants/` |
| [POST Favourite Restaurant](#post-favourite-restaurant) | `POST` | `/favourite-restaurants/` |
| [Blacklist Restaurants](#blacklist-restaurants)         | `GET`  | `/blacklist-restaurants/` |
| [POST Blacklist Restaurant](#post-blacklist-restaurant) | `POST` | `/blacklist-restaurants/` |
| [Next Restaurant](#next-restaurant)                     | `GET`  | `/next-restaurant/`       |
| [POST Restaurant](#post-restaurant)                     | `POST` | `/restaurant/`            |

<br>

### Tag & Ingredient APIs

| Name                                | Method | Path                |
| ----------------------------------- | ------ | ------------------- |
| [All Tags](#all-tags)               | `GET`  | `/all-tags/`        |
| [POST Tag](#post-tag)               | `POST` | `/tag/`             |
| [All Ingredients](#all-ingredients) | `GET`  | `/all-ingredients/` |
| [POST Ingredient](#post-ingredient) | `POST` | `/ingredient/`      |

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

<br>

> Log out

<br>

- Request body can be null. Only need the token.

- _Logout Successful_ Response:

  ```json
  { "detail": "Log out successfully." }
  ```

<br>

[^](#api-list)

---

## All Foods

<br>

> Get a list of all of the foods from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "bánh mì",
      "image": "/media/fallback.png",
      "description": "banh mi bnh mi banh mi banh mi",
      "address": "ai ma biet duoc",
      "recipe": "banh mi",
      "tags": [
        {
          "id": 1,
          "name": "ăn sáng",
          "description": "",
          "verified": true
        }
      ],
      "ingredients": [
        {
          "id": 1,
          "name": "bột mì",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    },
    {
      "id": 2,
      "name": "taiyaki đậu đỏ",
      "image": "/media/fallback.png",
      "description": "bánh cá Nhật Bản nhân đậu đỏ",
      "address": "",
      "recipe": "",
      "tags": [
        {
          "id": 2,
          "name": "ăn vặt",
          "description": "",
          "verified": true
        }
      ],
      "ingredients": [
        {
          "id": 1,
          "name": "bột mì",
          "description": "",
          "verified": true
        },
        {
          "id": 3,
          "name": "đậu đỏ",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    },
    {
      "id": 3,
      "name": "bánh rán",
      "image": "/media/images/foods/how.jpg",
      "description": "bánh rán nhân đỗ xanh tẩm đường giòn ngon nhưng ăn nhiều thì béo",
      "address": "",
      "recipe": "",
      "tags": [
        {
          "id": 2,
          "name": "ăn vặt",
          "description": "",
          "verified": true
        }
      ],
      "ingredients": [
        {
          "id": 2,
          "name": "bột nếp",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    }
  ]
  ```

<br>

[^](#api-list)

---

## Favourite Foods

<br>

> Get a list of user's favourite foods

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteFood": [
      {
        "id": 1,
        "name": "bánh mì",
        "image": "/media/fallback.png",
        "description": "banh mi bnh mi banh mi banh mi",
        "address": "ai ma biet duoc",
        "recipe": "banh mi",
        "tags": [
          {
            "id": 1,
            "name": "ăn sáng",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 1,
            "name": "bột mì",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
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

## POST Favourite Food

<br>

> Add food into your favourite list.

<br>

- Request example:

  ```json
  {
    "foodId": 2
  }
  ```

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteFood": [
      {
        "id": 1,
        "name": "bánh mì",
        "image": "/media/fallback.png",
        "description": "banh mi bnh mi banh mi banh mi",
        "address": "ai ma biet duoc",
        "recipe": "banh mi",
        "tags": [
          {
            "id": 1,
            "name": "ăn sáng",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 1,
            "name": "bột mì",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      },
      {
        "id": 2,
        "name": "taiyaki đậu đỏ",
        "image": "/media/fallback.png",
        "description": "bánh cá Nhật Bản nhân đậu đỏ",
        "address": "",
        "recipe": "",
        "tags": [
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 1,
            "name": "bột mì",
            "description": "",
            "verified": true
          },
          {
            "id": 3,
            "name": "đậu đỏ",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
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

## Blacklist Foods

<br>

> Get a list of user's blacklisted foods

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistFood": [
      {
        "id": 3,
        "name": "bánh rán",
        "image": "/media/images/foods/how.jpg",
        "description": "bánh rán nhân đỗ xanh tẩm đường giòn ngon nhưng ăn nhiều thì béo",
        "address": "",
        "recipe": "",
        "tags": [
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 2,
            "name": "bột nếp",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to blacklist foods."
  }
  ```

<br>

[^](#api-list)

---

## POST Blacklist Food

<br>

> Add food into your blacklist.

<br>

- Request example:

  ```json
  {
    "foodId": 2
  }
  ```

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistFood": [
      {
        "id": 2,
        "name": "taiyaki đậu đỏ",
        "image": "/media/fallback.png",
        "description": "bánh cá Nhật Bản nhân đậu đỏ",
        "address": "",
        "recipe": "",
        "tags": [
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 1,
            "name": "bột mì",
            "description": "",
            "verified": true
          },
          {
            "id": 3,
            "name": "đậu đỏ",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      },
      {
        "id": 3,
        "name": "bánh rán",
        "image": "/media/images/foods/how.jpg",
        "description": "bánh rán nhân đỗ xanh tẩm đường giòn ngon nhưng ăn nhiều thì béo",
        "address": "",
        "recipe": "",
        "tags": [
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "ingredients": [
          {
            "id": 2,
            "name": "bột nếp",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
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

## Next Food

<br>

> Get a random food from database

<br>

- Response example:

  ```json
  {
    "nextFood": {
      "id": 1,
      "name": "bánh mì",
      "image": "/media/fallback.png",
      "description": "banh mi bnh mi banh mi banh mi",
      "address": "ai ma biet duoc",
      "recipe": "banh mi",
      "tags": [
        {
          "id": 1,
          "name": "ăn sáng",
          "description": "",
          "verified": true
        }
      ],
      "ingredients": [
        {
          "id": 1,
          "name": "bột mì",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    }
  }
  ```

<br>

[^](#api-list)

---

## POST Food

<br>

> Post a new Food item to the system

<br>

- Request example:

  ```json
  {
    "name": "bánh nướng",
    "description": "nhân thập cẩm là số 1, nhân đậu xanh là tà đạo",
    "tags": [2]
  }
  ```

- Response example:

  ```json
  {
    "id": 6,
    "name": "bánh nướng",
    "image": "/media/fallback.png",
    "description": "nhân thập cẩm là số 1, nhân đậu xanh là tà đạo",
    "address": "",
    "recipe": "",
    "tags": [
      {
        "id": 2,
        "name": "ăn vặt",
        "description": "",
        "verified": true
      }
    ],
    "ingredients": [],
    "verified": false
  }
  ```

<br>

[^](#api-list)

---

## All Restaurants

<br>

> Get a list of all of the restaurants from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "tiem banh mi",
      "image": "/media/fallback.png",
      "description": "",
      "address": "tiem banh mi",
      "menu": "banh mi",
      "note": "banh mi",
      "tags": [
        {
          "id": 1,
          "name": "ăn sáng",
          "description": "",
          "verified": true
        },
        {
          "id": 2,
          "name": "ăn vặt",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    },
    {
      "id": 4,
      "name": "bánh trung thu Đông Phương",
      "image": "/media/fallback.png",
      "description": "hiệu bánh trung thu bán chạy nhất Hải Phòng hàng năm, nguyên nhân làm tắc đường Cầu Đất mỗi tháng 8",
      "address": "",
      "menu": "",
      "note": "",
      "tags": [
        {
          "id": 2,
          "name": "ăn vặt",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    }
  ]
  ```

<br>

[^](#api-list)

---

## Favourite Restaurants

<br>

> Get a list of user's favourite restaurants

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteRestaurant": [
      {
        "id": 1,
        "name": "tiem banh mi",
        "image": "/media/fallback.png",
        "description": "",
        "address": "tiem banh mi",
        "menu": "banh mi",
        "note": "banh mi",
        "tags": [
          {
            "id": 1,
            "name": "ăn sáng",
            "description": "",
            "verified": true
          },
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to have your favourite restaurants listed."
  }
  ```

<br>

[^](#api-list)

---

## POST Favourite Restaurant

<br>

> Add restaurant into your favourite list.

<br>

- Request example:

  ```json
  {
    "restaurantId": 2
  }
  ```

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteRestaurant": [
      {
        "id": 1,
        "name": "tiem banh mi",
        "image": "/media/fallback.png",
        "description": "",
        "address": "tiem banh mi",
        "menu": "banh mi",
        "note": "banh mi",
        "tags": [
          {
            "id": 1,
            "name": "ăn sáng",
            "description": "",
            "verified": true
          },
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      },
      {
        "id": 36,
        "name": "phở có hành?",
        "image": "/media/fallback.png",
        "description": "thêm vào để blacklist",
        "address": "",
        "menu": "",
        "note": "hành ~~ rất nhiều hành",
        "tags": [],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to have your favourite restaurants listed."
  }
  ```

<br>

[^](#api-list)

---

## Blacklist Restaurants

<br>

> Get a list of user's blacklisted restaurants

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistRestaurant": [
      {
        "id": 36,
        "name": "phở có hành?",
        "image": "/media/fallback.png",
        "description": "thêm vào để blacklist",
        "address": "",
        "menu": "",
        "note": "hành ~~ rất nhiều hành",
        "tags": [],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to blacklist restaurants."
  }
  ```

<br>

[^](#api-list)

---

## POST Blacklist Restaurant

<br>

> Add restaurant into your blacklist.

<br>

- Request example:

  ```json
  {
    "restaurantId": 35
  }
  ```

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistRestaurant": [
      {
        "id": 35,
        "name": "bánh trung thu Đông Phương",
        "image": "/media/fallback.png",
        "description": "hiệu bánh trung thu bán chạy nhất Hải Phòng hàng năm, nguyên nhân làm tắc đường Cầu Đất mỗi tháng 8",
        "address": "",
        "menu": "",
        "note": "",
        "tags": [
          {
            "id": 2,
            "name": "ăn vặt",
            "description": "",
            "verified": true
          }
        ],
        "verified": true
      },
      {
        "id": 36,
        "name": "phở có hành?",
        "image": "/media/fallback.png",
        "description": "thêm vào để blacklist",
        "address": "",
        "menu": "",
        "note": "hành ~~ rất nhiều hành",
        "tags": [],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to blacklist restaurants."
  }
  ```

<br>

[^](#api-list)

---

## Next Restaurant

<br>

> Get a random restaurant from database

<br>

- Response example:

  ```json
  {
    "nextRestaurant": {
      "id": 4,
      "name": "bánh trung thu Đông Phương",
      "image": "/media/fallback.png",
      "description": "hiệu bánh trung thu bán chạy nhất Hải Phòng hàng năm, nguyên nhân làm tắc đường Cầu Đất mỗi tháng 8",
      "address": "",
      "menu": "",
      "note": "",
      "tags": [
        {
          "id": 2,
          "name": "ăn vặt",
          "description": "",
          "verified": true
        }
      ],
      "verified": true
    }
  }
  ```

<br>

[^](#api-list)

---

## POST Restaurant

<br>

> Post a new Restaurant item to the system

<br>

- Request example:

  ```json
  {
    "name": "bánh trung thu Đông Phương",
    "description": "hiệu bánh trung thu bán chạy nhất Hải Phòng hàng năm, nguyên nhân làm tắc đường Cầu Đất mỗi tháng 8",
    "tags": [2]
  }
  ```

- Response example:

  ```json
  {
    "id": 35,
    "name": "bánh trung thu Đông Phương",
    "image": "/media/fallback.png",
    "description": "hiệu bánh trung thu bán chạy nhất Hải Phòng hàng năm, nguyên nhân làm tắc đường Cầu Đất mỗi tháng 8",
    "address": "",
    "menu": "",
    "note": "",
    "tags": [
      {
        "id": 2,
        "name": "ăn vặt",
        "description": "",
        "verified": true
      }
    ],
    "verified": true
  }
  ```

<br>

[^](#api-list)

---

## All Tags

<br>

> Get a list of all of the tags from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "ăn sáng",
      "description": "",
      "verified": true
    },
    {
      "id": 2,
      "name": "ăn vặt",
      "description": "",
      "verified": true
    }
  ]
  ```

<br>

[^](#api-list)

---

## POST Tag

<br>

> Post a new Tag item to the system

<br>

- Request example:

  ```json
  {
    "name": "ăn trưa"
  }
  ```

- Response example:

  ```json
  {
    "id": 5,
    "name": "ăn trưa",
    "description": "",
    "verified": false
  }
  ```

<br>

[^](#api-list)

---

## All Ingredients

<br>

> Get a list of all of the ingredients from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "bột mì",
      "description": "",
      "verified": true
    },
    {
      "id": 2,
      "name": "bột nếp",
      "description": "",
      "verified": true
    },
    {
      "id": 3,
      "name": "đậu đỏ",
      "description": "",
      "verified": true
    }
  ]
  ```

<br>

[^](#api-list)

---

## POST Ingredient

<br>

> Post a new Ingredient item to the system

<br>

- Request example:

  ```json
  {
    "name": "thịt heo"
  }
  ```

- Response example:

  ```json
  {
    "id": 4,
    "name": "thịt heo",
    "description": "",
    "verified": false
  }
  ```

<br>

[^](#api-list)

---
