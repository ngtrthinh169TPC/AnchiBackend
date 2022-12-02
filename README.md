# AnchiBackend

Backend for Anchi - A project for my school homework.

This project is currently (2022) being deployed [here](https://anchi-api.aqaurius6666.space/).

<br>

---

<br>

## API List

Click the name of API for more details.

// TODO: add api names to all detail sections

### User APIs

| Name                                | Method | Path                |
| ----------------------------------- | ------ | ------------------- |
| [Register](#register-api)           | `POST` | `/user/`            |
| [Login](#login-api)                 | `POST` | `/login/`           |
| [Logout](#logout)                   | `POST` | `/logout/`          |
| [Change Password](#change-password) | `POST` | `/change-password/` |

<br>

### Food APIs

| Name                                            | Method  | Path                |
| ----------------------------------------------- | ------- | ------------------- |
| [All Foods](#all-foods)                         | `GET`   | `/all-foods/`       |
| [GET Favourite Foods](#get-favourite-foods)     | `GET`   | `/favourite-foods/` |
| [POST Favourite Food](#post-favourite-food)     | `POST`  | `/favourite-foods/` |
| [PATCH Favourite Foods](#patch-favourite-foods) | `PATCH` | `/favourite-foods/` |
| [GET Blacklist Foods](#get-blacklist-foods)     | `GET`   | `/blacklist-foods/` |
| [POST Blacklist Food](#post-blacklist-food)     | `POST`  | `/blacklist-foods/` |
| [PATCH Blacklist Foods](#patch-blacklist-foods) | `PATCH` | `/blacklist-foods/` |
| [Next Food](#next-food)                         | `GET`   | `/next-food/`       |
| [POST Food](#post-food)                         | `POST`  | `/food/`            |

<br>

### Restaurant APIs

| Name                                                        | Method  | Path                      |
| ----------------------------------------------------------- | ------- | ------------------------- |
| [All Restaurants](#all-restaurants)                         | `GET`   | `/all-restaurants/`       |
| [GET Favourite Restaurants](#get-favourite-restaurants)     | `GET`   | `/favourite-restaurants/` |
| [POST Favourite Restaurant](#post-favourite-restaurant)     | `POST`  | `/favourite-restaurants/` |
| [PATCH Favourite Restaurants](#patch-favourite-restaurants) | `PATCH` | `/favourite-restaurants/` |
| [GET Blacklist Restaurants](#get-blacklist-restaurants)     | `GET`   | `/blacklist-restaurants/` |
| [POST Blacklist Restaurant](#post-blacklist-restaurant)     | `POST`  | `/blacklist-restaurants/` |
| [PATCH Blacklist Restaurants](#patch-blacklist-restaurants) | `PATCH` | `/blacklist-restaurants/` |
| [Next Restaurant](#next-restaurant)                         | `GET`   | `/next-restaurant/`       |
| [POST Restaurant](#post-restaurant)                         | `POST`  | `/restaurant/`            |

<br>

### Tag & Ingredient & Area APIs

| Name                                | Method | Path                |
| ----------------------------------- | ------ | ------------------- |
| [All Tags](#all-tags)               | `GET`  | `/all-tags/`        |
| [POST Tag](#post-tag)               | `POST` | `/tag/`             |
| [All Ingredients](#all-ingredients) | `GET`  | `/all-ingredients/` |
| [POST Ingredient](#post-ingredient) | `POST` | `/ingredient/`      |
| [All Areas](#all-areas)             | `GET`  | `/all-areas/`       |
| [POST Area](#post-area)             | `POST` | `/area/`            |

<br>

---

<br>

## Register API

<br>

> Register a new User.

- API: `/user/`

<br>

- Request example:

  ```json
  {
    "username": "Minh Huong",
    "password": "minhehe123",
    "email": "khongphaimh@gmail.com"
  }
  ```

- Response example:

  ```json
  {
    "username": "Minh Huong",
    "token": "b48d7ff8fd3de7417c451156a7516fc75aecf40d",
    "email": "khongphaimh@gmail.com"
  }
  ```

<br>

[^](#user-apis)

---

<br>

## Login API

<br>

> Log in as an User.

- API: `/login/`

<br>

- Request example:

  ```json
  { "username": "Minh Huong", "password": "minhehe123" }
  ```

- _Login Successful_ Response example:

  ```json
  {
    "username": "Minh Huong",
    "token": "b48d7ff8fd3de7417c451156a7516fc75aecf40d",
    "email": "khongphaimh@gmail.com"
  }
  ```

- _Login Failed_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#user-apis)

---

## Logout

<br>

> Log out

- API: `/logout/`

<br>

- Request body can be null. Only need the token.

- _Logout Successful_ Response:

  ```json
  { "detail": "Log out successfully." }
  ```

<br>

[^](#user-apis)

---

## Change Password

<br>

> Change password using the old password

<br>

- Request example:

  ```json
  {
    "username": "Minh Huong",
    "password": "minhehe123",
    "new_password": "minhehe124"
  }
  ```

- _Change Password Successful_ Response:

  ```json
  {
    "detail": "Your password has been changed successfully."
  }
  ```

- _Wrong user credential_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

- _Duplicated password_ Response:

  ```json
  {
    "detail": "Your new password should be different from the old password."
  }
  ```

- _No new password provided_ Response:

  ```json
  {
    "detail": "Missing new_password field."
  }
  ```

<br>

[^](#user-apis)

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
      "areas": [],
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
      "areas": [],
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
      "areas": [],
      "verified": true
    }
  ]
  ```

<br>

[^](#food-apis)

---

## GET Favourite Foods

<br>

> Get a list of user's favourite foods

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteFoods": [
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
        "areas": [],
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

[^](#food-apis)

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
    "favouriteFoods": [
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
        "areas": [],
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
        "areas": [],
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

- _Food id not found_ Response:

  ```json
  {
    "detail": "Provided food is not found at food_id 7"
  }
  ```

- _Food not found_ Response:

  ```json
  {
    "detail": "You must provide a food in order add to your favourite list"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#food-apis)

---

## PATCH Favourite Foods

<br>

> Edit your favourite food list.

<br>

- Request example:

  ```json
  {
    "favouriteFoods": [2, 6]
  }
  ```

- Response example:

  ```json
  {
    "username": "user002",
    "favouriteFoods": [
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
        "areas": [],
        "verified": true
      },
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
        "areas": [],
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

- _Food id not found_ Response:

  ```json
  {
    "detail": "Provided food is not found at food_id 7"
  }
  ```

- _List not found_ Response:

  ```json
  {
    "detail": "You must provide a list to update your favourite foods"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#food-apis)

---

## GET Blacklist Foods

<br>

> Get a list of user's blacklisted foods

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistFoods": [
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
        "areas": [],
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

[^](#food-apis)

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
    "blacklistFoods": [
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
        "areas": [],
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
        "areas": [],
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

- _Food id not found_ Response:

  ```json
  {
    "detail": "Provided food is not found at food_id 7"
  }
  ```

- _Food not found_ Response:

  ```json
  {
    "detail": "You must provide a food in order add to your blacklist"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#food-apis)

---

## PATCH Blacklist Foods

<br>

> Edit your food blacklist.

<br>

- Request example:

  ```json
  {
    "blacklistFoods": [3]
  }
  ```

- Response example:

  ```json
  {
    "username": "user002",
    "blacklistFoods": [
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
        "areas": [],
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

- _Food id not found_ Response:

  ```json
  {
    "detail": "Provided food is not found at food_id 7"
  }
  ```

- _List not found_ Response:

  ```json
  {
    "detail": "You must provide a list to update your blacklist foods"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#food-apis)

---

## Next Food

<br>

> Get a random food from database

<br>

- Request body can be null.

- Request example

  ```json
  {
    "lastFood": 2
  }
  ```

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
      "areas": [],
      "verified": true
    }
  }
  ```

- Response _not found_:

  ```json
  {
    "detail": "We don't have any foods left :( come again later or try add some foods for us."
  }
  ```

<br>

[^](#food-apis)

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
    "areas": [],
    "verified": false
  }
  ```

<br>

[^](#food-apis)

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
      "areas": [],
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
      "areas": [],
      "verified": true
    }
  ]
  ```

<br>

[^](#restaurant-apis)

---

## GET Favourite Restaurants

<br>

> Get a list of user's favourite restaurants

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "favouriteRestaurants": [
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
        "areas": [],
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

[^](#restaurant-apis)

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
    "favouriteRestaurants": [
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
        "areas": [],
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
        "areas": [],
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

- _Restaurant id not found_ Response:

  ```json
  {
    "detail": "Provided restaurant is not found at restaurant_id 6"
  }
  ```

- _Restaurant not found_ Response:

  ```json
  {
    "detail": "You must provide a restaurant in order add to your favourite list"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#restaurant-apis)

---

## PATCH Favourite Restaurants

<br>

> Edit your favourite restaurant list.

<br>

- Request example:

  ```json
  {
    "favouriteRestaurants": [1]
  }
  ```

- Response example:

  ```json
  {
    "username": "user002",
    "favouriteRestaurants": [
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
        "areas": [],
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

- _Restaurant id not found_ Response:

  ```json
  {
    "detail": "Provided restaurant is not found at restaurant_id 3"
  }
  ```

- _List not found_ Response:

  ```json
  {
    "detail": "You must provide a list to update your favourite restaurants"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#restaurant-apis)

---

## GET Blacklist Restaurants

<br>

> Get a list of user's blacklisted restaurants

<br>

- Response example:

  ```json
  {
    "username": "user003",
    "blacklistRestaurants": [
      {
        "id": 36,
        "name": "phở có hành?",
        "image": "/media/fallback.png",
        "description": "thêm vào để blacklist",
        "address": "",
        "menu": "",
        "note": "hành ~~ rất nhiều hành",
        "tags": [],
        "areas": [],
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

[^](#restaurant-apis)

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
    "blacklistRestaurants": [
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
        "areas": [],
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
        "areas": [],
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

- _Restaurant id not found_ Response:

  ```json
  {
    "detail": "Provided restaurant is not found at restaurant_id 6"
  }
  ```

- _Restaurant not found_ Response:

  ```json
  {
    "detail": "You must provide a restaurant in order add to your blacklist"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#restaurant-apis)

---

## PATCH Blacklist Restaurants

<br>

> Edit your restaurant blacklist.

<br>

- Request example:

  ```json
  {
    "blacklistRestaurants": [36]
  }
  ```

- Response example:

  ```json
  {
    "username": "user002",
    "blacklistRestaurants": [
      {
        "id": 36,
        "name": "phở có hành?",
        "image": "/media/fallback.png",
        "description": "thêm vào để blacklist",
        "address": "",
        "menu": "",
        "note": "hành ~~ rất nhiều hành",
        "tags": [],
        "areas": [],
        "verified": true
      }
    ]
  }
  ```

- _Anonymous User_ Response:

  ```json
  {
    "detail": "You must sign in to have your blacklist restaurants listed."
  }
  ```

- _Restaurant id not found_ Response:

  ```json
  {
    "detail": "Provided restaurant is not found at restaurant_id 6"
  }
  ```

- _List not found_ Response:

  ```json
  {
    "detail": "You must provide a list to update your blacklist restaurants"
  }
  ```

- _Not AnchiUser_ Response:

  ```json
  {
    "detail": "Invalid user credentials."
  }
  ```

<br>

[^](#restaurant-apis)

---

## Next Restaurant

<br>

> Get a random restaurant from database

<br>

- Request body can be null.

- Request example

  ```json
  {
    "lastRestaurant": 2
  }
  ```

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
      "areas": [],
      "verified": true
    }
  }
  ```

- Response _not found_:

  ```json
  {
    "detail": "We don't have any food restaurants left :( come again later or try add some restaurants for us."
  }
  ```

<br>

[^](#restaurant-apis)

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
    "areas": [],
    "verified": true
  }
  ```

<br>

[^](#restaurant-apis)

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

[^](#tag--ingredient--area-apis)

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

[^](#tag--ingredient--area-apis)

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

[^](#tag--ingredient--area-apis)

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

[^](#tag--ingredient--area-apis)

---

## All Areas

<br>

> Get a list of all of the areas from database

<br>

- Response example:

  ```json
  [
    {
      "id": 1,
      "name": "ĐHQG - ĐHSP",
      "description": "",
      "verified": true
    }
  ]
  ```

<br>

[^](#tag--ingredient--area-apis)

---

## POST Area

<br>

> Post a new Area item to the system

<br>

- Request example:

  ```json
  {
    "name": "Nghĩa Tân - Cầu Giấy"
  }
  ```

- Response example:

  ```json
  {
    "id": 2,
    "name": "Nghĩa Tân - Cầu Giấy",
    "description": "",
    "verified": false
  }
  ```

<br>

[^](#tag--ingredient--area-apis)

---

```

```
