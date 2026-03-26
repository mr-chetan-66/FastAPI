# 1️⃣ POST – Create User
# POST /users

# Python{  "id": 1,  "name": "Shrihari",  "email": "shrihari@gmail.com",  "phone": "9999999999",  "default_location": "Bangalore",  "preferred_payment": "UPI"}

# 2️⃣ GET – All Users
# GET /users


# 3️⃣ GET – One User
# GET /users/1


# 4️⃣ PUT – Replace Entire User
# PUT /users/1

# JSON{  "id": 1,  "name": "Chetan",  "email": "chetan@gmail.com",  "phone": "8888888888",  "default_location": "Mumbai",  "preferred_payment": "Card"}``Show more lines

# 5️⃣ PATCH – Update Partial Fields
# PATCH /users/1

# JSON{  "phone": "7777777777"}Show more lines

# 6️⃣ DELETE – Remove User
# DELETE /users/1

# -------------------------------------------------------------------
# |   ACTION                     | MEANING            | HTTP METHOD |
# -------------------------------------------------------------------
# | "I want to read a book"      | Show details       | GET         |
# | "I want to replace this book"| Replace full book  | PUT         |
# | "I want to update a page"    | Partial update     | PATCH       |
# | "I want to add a book"       | Create             | POST        |
# | "I want to remove a book"    | Delete             | DELETE      |
# -------------------------------------------------------------------