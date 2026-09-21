def get_user_role():

    email = get_current_email()

    if not email:
        return None

    email = email.lower().strip()

    # Academy Director
    if email == "boomattolatunji@gmail.com":
        return "admin"

    # Tutor
    if email == "test@gmail.com":
        return "tutor"

    return "unknown"
