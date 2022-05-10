from datetime import date, datetime


def dob_check(userdob):
    """
    returns true if the user is older than 18
    """
    now = date.today()
    if isinstance(userdob, str):

        userdob = datetime.strptime(
            userdob.replace("-", " "), "%Y %m %d"
        )

    age = (
        now.year
        - userdob.year
        - ((now.month, now.day) < (userdob.month, userdob.day))
    )

    if age > 18:
        return True
    else:
        return False
