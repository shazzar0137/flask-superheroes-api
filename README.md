#  Flask Superheroes API

##  Project Overview

It is a RESTful API built with Flask that manages a database of superheroes and their powers. It allows you to:

* View all superheroes and their super names.
* View individual heroes with their associated powers.
* View and update superpowers.
* Assign powers to heroes with strength levels.

This project demonstrates relational database modeling, route handling, serialization, validations, and use of Postman for API testing.

---

## 📁 Project Structure

```
flask-superheroes-api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── seed.py
│   ├── config.py
│
├── instance/
│   └── app.db
│
├── migrations/
│   └── (Flask-Migrate generated files)
│
├── manage.py
├──  Pipfile
├── Pipfile.lock
├── README.md
└── challenge-2-superheroes.postman_collection.json
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shazzar0137/flask-superheroes-api.git
cd flask-superheroes-api
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies



```bash
pip install pipenv
pipenv install
```



### 4. Set Environment Variable

```bash
export FLASK_APP=manage.py
```


### 5. Run Migrations

```bash
flask db init      
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Seed the Database

```bash
python app/seed.py
```

### 7. Run the Server

```bash
flask run
```

> Server runs by default at: [http://127.0.0.1:5000](http://127.0.0.1:5000)
> Or at port 5555 if specified in `manage.py` as: `app.run(port=5555, debug=True)`

---

## 📬 Postman Setup

1. Open [Postman](https://www.postman.com/downloads/)
2. Click "Import"
3. Choose `challenge-2-superheroes.postman_collection.json` from this repo
4. Run the saved requests to test your endpoints

---

## 📌 API Endpoints

### 🔹 GET `/heroes`

**Returns a list of all heroes.**

```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  ...
]
```

---

### 🔹 GET `/heroes/:id`

* If Hero found:

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "hero_id": 1,
      "power_id": 2,
      "strength": "Strong",
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly..."
      }
    }
  ]
}
```

* If Hero not found:

```json
{
  "error": "Hero not found"
}
```

---

### 🔹 GET `/powers`

**Returns all powers.**

```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  },
  ...
]
```

---

### 🔹 GET `/powers/:id`

* If found:

```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

* If not found:

```json
{
  "error": "Power not found"
}
```

---

### 🔹 PATCH `/powers/:id`

**Update power's description **

**Request body:**

```json
{
  "description": "Updated description at least 20 chars"
}
```

* On success:

```json
{
  "id": 1,
  "name": "super strength",
  "description": "Updated description at least 20 chars"
}
```

* On failure:

```json
{
  "errors": ["validation errors"]
}
```

---

### 🔹 POST `/hero_powers`

**Assign a power to a hero.**

**Request body:**

```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

* On success:

```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
```

* On failure:

```json
{
  "errors": ["validation errors"]
}
```

---

## Validations

* `Power.description` must be **present** and at least **20 characters** long.
* `HeroPower.strength` must be one of: **"Strong"**, **"Weak"**, or **"Average"**.

---

##  Technologies Used

* Python 3.x
* Flask
* Flask SQLAlchemy
* Flask Migrate
* SQLite
* Postman (for testing)

---

##  Author

Daniel Kipngetioch
Software Engineering Student @ Moringa School
GitHub: https://github.com/shazzar0137/flask-superheroes-api

---

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
