import streamlit as st
from supabase_client import supabase

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚"
)

st.title("📚 Boomatt Academy")


# LOGIN
if "user" not in st.session_state:

    st.subheader("Portal Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if response.user:

                st.session_state.user = response.user

                st.success("Login successful!")

                st.rerun()

        except Exception as e:

            st.error(f"Login failed: {e}")

    st.stop()


# USER INFORMATION
user = st.session_state.user

email = user.email

st.success("Login successful.")

st.write("Logged in email:")
st.code(email)


# ROLE DETECTION
if email.lower().strip() == "boomattolatunji@gmail.com":

    role = "admin"

elif email.lower().strip() == "test@gmail.com":

    role = "tutor"

else:

    role = "unknown"


st.write("Detected role:")
st.code(role)


# TUTOR PORTAL
if role == "tutor":

    st.title("👨‍🏫 Tutor Portal")

    st.success(
        "Welcome to the Boomatt Academy Tutor Portal."
    )

    st.write(f"Tutor account: {email}")

    st.divider()

    st.header("My Dashboard")

    st.write("Your tutor portal is working.")

    if st.button("Logout"):

        supabase.auth.sign_out()

        st.session_state.clear()

        st.rerun()


# ADMIN PORTAL
elif role == "admin":

    st.title("👨‍💼 Admin Portal")

    st.success(
        "Welcome to the Boomatt Academy Admin Portal."
    )

    if st.button("Logout"):

        supabase.auth.sign_out()

        st.session_state.clear()

        st.rerun()


# UNKNOWN
else:

    st.error(
        "This account has not been assigned a portal role."
    )

    if st.button("Logout"):

        supabase.auth.sign_out()

        st.session_state.clear()

        st.rerun()
