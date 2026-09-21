import streamlit as st
from supabase_client import supabase

st.set_page_config(
    page_title="Boomatt Academy | Admin Portal",
    page_icon="📚",
    layout="wide"
)

st.success("Supabase connection loaded successfully.")
)

# -----------------------------
# HEADER
# -----------------------------

st.title("📚 Boomatt Academy")
st.caption("Building Confident Learners, One Lesson at a Time")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Admin Portal")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Students",
        "Tutors",
        "Parents",
        "Timetable",
        "Attendance",
        "Lesson Reports",
        "Payments"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    st.header("Welcome, Academy Director 👋")

    st.write(
        "This is your central Boomatt Academy management dashboard."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Students", "0")

    with col2:
        st.metric("Tutors", "0")

    with col3:
        st.metric("Parents", "0")

    with col4:
        st.metric("Active Classes", "0")

    st.divider()

    st.subheader("Academy Overview")

    st.info(
        "Your academy management system is being built. "
        "Students, tutors, parents, schedules, attendance, "
        "reports and payments will be connected to this dashboard."
    )


# -----------------------------
# STUDENTS
# -----------------------------

elif page == "Students":

    st.header("🎓 Students")

    st.write("Manage Boomatt Academy students.")

    with st.form("student_form"):

        name = st.text_input("Student Name")
        year = st.text_input("Year / Grade")
        school = st.text_input("School")
        subjects = st.text_input("Subjects")

        submitted = st.form_submit_button("Add Student")

        if submitted:

            if name:
                st.success(f"{name} has been added.")
            else:
                st.warning("Please enter the student's name.")


# -----------------------------
# TUTORS
# -----------------------------

elif page == "Tutors":

    st.header("👨‍🏫 Tutors")

    st.write("Manage Boomatt Academy tutors.")

    with st.form("tutor_form"):

        name = st.text_input("Tutor Name")
        subjects = st.text_input("Subjects Taught")
        qualification = st.text_input("Qualification")

        submitted = st.form_submit_button("Add Tutor")

        if submitted:

            if name:
                st.success(f"{name} has been added.")
            else:
                st.warning("Please enter the tutor's name.")


# -----------------------------
# PARENTS
# -----------------------------

elif page == "Parents":

    st.header("👨‍👩‍👧 Parents")

    st.write("Manage parent accounts and student relationships.")

    with st.form("parent_form"):

        name = st.text_input("Parent / Guardian Name")
        email = st.text_input("Email Address")

        submitted = st.form_submit_button("Add Parent")

        if submitted:

            if name:
                st.success(f"{name} has been added.")
            else:
                st.warning("Please enter the parent's name.")


# -----------------------------
# TIMETABLE
# -----------------------------

elif page == "Timetable":

    st.header("📅 Timetable")

    st.write("Manage lessons and tutor schedules.")

    st.info(
        "The timetable system will allow you to assign "
        "students, tutors, subjects, dates and lesson times."
    )


# -----------------------------
# ATTENDANCE
# -----------------------------

elif page == "Attendance":

    st.header("✅ Attendance")

    st.write("Monitor lesson attendance.")

    st.info(
        "Tutors will eventually be able to mark students "
        "as Present, Absent or Rescheduled."
    )


# -----------------------------
# LESSON REPORTS
# -----------------------------

elif page == "Lesson Reports":

    st.header("📝 Lesson Reports")

    st.write("View tutor lesson reports and student feedback.")

    st.info(
        "Tutors will submit lesson summaries, topics covered, "
        "homework and areas requiring further attention."
    )


# -----------------------------
# PAYMENTS
# -----------------------------

elif page == "Payments":

    st.header("💰 Payments")

    st.write("Monitor academy payments.")

    st.info(
        "The payment section will eventually track invoices, "
        "payment status, lesson packages and outstanding balances."
    )
