from datetime import date

def dob_check(userdob):
# """
# returns true if the user is older than 18
# """
    now = date.today()
    age = now.year - userdob.year - ((now.month, now.day) < (userdob.month, userdob.day))
    print(age)
    if age > 18:
        return True
    else:
        return False