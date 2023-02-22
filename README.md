# fastapi-authapp-learn


# main.py
contains the routes


# database/database.py
all necessary functions to init a Database 

# commons/crud.py
contains all the C.R.U.D functionalty

# commons/auth.py
in the auth.py file is the logic of the password hash and verify functionalty 
for this we use the passlib liberay to generate a password hash.
after the db session connection we have to verify the password with the hashed password

