from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def create_password_hash(password: str) -> str:
    """create a hashed password by given the password

    Args:
        password (str): given password as string

    Returns:
        str: hashed password
    """
    return pwd_context.hash(password)

def verify_pwassword(plain_password: str, hashed_password: str) -> bool:
    """verify the password form the database

    Args:
        plain_password (str): given password by user
        hashed_password (str): hashed password from the database

    Returns:
        bool: True = if the given password is correct password in the DB 
              False = if the given password is not correct password in the DB
    """
    return pwd_context.verify(plain_password, hashed_password)