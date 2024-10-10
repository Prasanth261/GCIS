def validate(userid,password):
    if userid != "prasanth" or password != "Pass123": 
        raise ValueError("Invalid Username or Password")

def login():
    attemps=2
    for i in range(attemps):
     attemps-=1
     userid=input("Enter Username: ")
     password=input("Enter password: ")
     try:
      validate(userid,password)
      print("Logged In")
      break
     except ValueError:
        print("Wrong Password or Username")
    if attemps==0:
        raise ValueError("Attemplts are exhausted")
def main():
    try:
        login()
    except ValueError:
        print("ACCOUNT LOCKED, CONTACT YOUR ORGANIZATION ADMIN")

if __name__=="__main__":
    main()