def password():
    pwd=input("Enter a Password between 10-20 characters:")
    if len(pwd)<=10 or len(pwd) >=20:
        raise ValueError("Password must be b/w 100 and 20 charcters.")
    confirm_pwd=input("Confirm Password: ")

    if pwd != confirm_pwd:
        raise ValueError("Passwords must match!")
    
    return pwd
password()