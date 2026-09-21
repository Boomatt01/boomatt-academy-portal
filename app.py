import streamlit as st
from supabase_client import supabase

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚",
    layout="wide"
)


# =========================================================
# LOGIN
# =========================================================

if "user" not in st.session_state:
    st.session_state.user = None


if st.session_state.user is None:

    st.title("📚 Boomatt Academy")
    st.subheader("Admin Portal")
    st.caption("Building Confident Learners, One Lesson at a Time")

    st.divider()

    st.write("### Admin Login")

    email = st.text_input(
        "Email address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    if st.button("Login", type="primary"):

        if not email or not password:
            st.warning("Please enter your email and password.")

        else:

            try:

                response = supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })

                st.session_state.user = response.user

                st.success("Login successful.")

                st.rerun()

            except Exception:
                st.error(
                    "Login failed. Please check your email and password."
                )

    st.stop()


# =========================================================
# ADMIN PORTAL
# =========================================================

st.title("📚 Boomatt Academy")
st.caption("Building Confident Learners, One Lesson at a Time")

st.success("You are logged in as Academy Administrator.")

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Admin Portal")

st.sidebar.write(
    f"Logged in as: {st.session_state.user.email}"
)

if st.sidebar.button("Logout"):

    supabase.auth.sign_out()

    st.session_state.user = None

    st.rerun()


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


# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.header("Welcome, Academy Director 👋")

    st.write(
        "This is your central Boomatt Academy management dashboard."
    )

    col1, col2, col3, col4 = st.columns(4)

    try:
        students = supabase.table("Student").select("*").execute()
        student_count = len(students.data)

    except Exception:
        student_count = 0

    try:
        tutors = supabase.table("tutors").select("*").execute()
        tutor_count = len(tutors.data)

    except Exception:
        tutor_count = 0

    try:
        parents = supabase.table("parents").select("*").execute()
        parent_count = len(parents.data)

    except Exception:
        parent_count = 0

    try:
        timetable = supabase.table("timetable").select("*").execute()
        class_count = len(timetable.data)

    except Exception:
        class_count = 0

    with col1:
        st.metric("Students", student_count)

    with col2:
        st.metric("Tutors", tutor_count)

    with col3:
        st.metric("Parents", parent_count)

    with col4:
        st.metric("Classes", class_count)

    st.divider()

    st.subheader("Academy Overview")

    st.info(
        "The Boomatt Academy management system is connected "
        "to Supabase. You can now manage academy records "
        "through the Admin Portal."
    )


# =========================================================
# STUDENTS
# =========================================================

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

            if not name:
                st.warning("Please enter the student's name.")

            else:

                try:

                    supabase.table("Student").insert({
                        "full_name": name,
                        "year_grade": year,
                        "school": school,
                        "subjects": subjects
                    }).execute()

                    st.success(
                        f"{name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add student: {e}"
                    )


# =========================================================
# TUTORS
# =========================================================

elif page == "Tutors":

    st.header("👨‍🏫 Tutors")

    st.write("Manage Boomatt Academy tutors.")

    with st.form("tutor_form"):

        name = st.text_input("Tutor Name")
        email = st.text_input("Email Address")
        subjects = st.text_input("Subjects Taught")
        qualification = st.text_input("Qualification")

        submitted = st.form_submit_button("Add Tutor")

        if submitted:

            if not name:
                st.warning("Please enter the tutor's name.")

            else:

                try:

                    supabase.table("tutors").insert({
                        "full_name": name,
                        "email": email,
                        "subjects": subjects,
                        "qualification": qualification
                    }).execute()

                    st.success(
                        f"{name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add tutor: {e}"
                    )


# =========================================================
# PARENTS
# =========================================================

elif page == "Parents":

    st.header("👨‍👩‍👧 Parents")

    st.write(
        "Manage parent accounts and student relationships."
    )

    with st.form("parent_form"):

        name = st.text_input("Parent / Guardian Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")

        submitted = st.form_submit_button("Add Parent")

        if submitted:

            if not name:
                st.warning("Please enter the parent's name.")

            else:

                try:

                    supabase.table("parents").insert({
                        "full_name": name,
                        "email": email,
                        "phone": phone
                    }).execute()

                    st.success(
                        f"{name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add parent: {e}"
                    )


# =========================================================
# TIMETABLE
# =========================================================

elif page == "Timetable":

    st.header("📅 Timetable")

    st.write("Manage lessons and tutor schedules.")

    with st.form("timetable_form"):

        student = st.text_input("Student Name")
        tutor = st.text_input("Tutor Name")
        subject = st.text_input("Subject")
        day = st.selectbox(
            "Day",
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ]
        )

        start_time = st.text_input("Start Time")
        end_time = st.text_input("End Time")

        status = st.selectbox(
            "Status",
            ["Active", "Paused", "Completed", "Cancelled"]
        )

        submitted = st.form_submit_button(
            "Add Lesson"
        )

        if submitted:

            if not student or not tutor or not subject:
                st.warning(
                    "Please enter the student, tutor and subject."
                )

            else:

                try:

                    supabase.table("timetable").insert({
                        "student_name": student,
                        "tutor_name": tutor,
                        "subject": subject,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time,
                        "status": status
                    }).execute()

                    st.success(
                        "Lesson added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add lesson: {e}"
                    )


# =========================================================
# ATTENDANCE
# =========================================================

elif page == "Attendance":

    st.header("✅ Attendance")

    st.write("Record lesson attendance.")

    with st.form("attendance_form"):

        student = st.text_input("Student Name")
        tutor = st.text_input("Tutor Name")
        subject = st.text_input("Subject")
        lesson_date = st.date_input("Lesson Date")

        status = st.selectbox(
            "Attendance Status",
            [
                "Present",
                "Absent",
                "Rescheduled"
            ]
        )

        notes = st.text_area("Notes")

        submitted = st.form_submit_button(
            "Save Attendance"
        )

        if submitted:

            if not student or not tutor:
                st.warning(
                    "Please enter the student and tutor."
                )

            else:

                try:

                    supabase.table("attendance").insert({
                        "student_name": student,
                        "tutor_name": tutor,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "status": status,
                        "notes": notes
                    }).execute()

                    st.success(
                        "Attendance saved successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not save attendance: {e}"
                    )


# =========================================================
# LESSON REPORTS
# =========================================================

elif page == "Lesson Reports":

    st.header("📝 Lesson Reports")

    st.write(
        "Record tutor lesson reports and student feedback."
    )

    with st.form("lesson_report_form"):

        student = st.text_input("Student Name")
        tutor = st.text_input("Tutor Name")
        subject = st.text_input("Subject")
        lesson_date = st.date_input("Lesson Date")

        topic = st.text_input("Topic Covered")

        lesson_summary = st.text_area(
            "Lesson Summary"
        )

        homework = st.text_area(
            "Homework"
        )

        areas_to_improve = st.text_area(
            "Areas to Improve"
        )

        submitted = st.form_submit_button(
            "Save Lesson Report"
        )

        if submitted:

            if not student or not tutor:
                st.warning(
                    "Please enter the student and tutor."
                )

            else:

                try:

                    supabase.table("lesson_reports").insert({
                        "student_name": student,
                        "tutor_name": tutor,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "topic": topic,
                        "lesson_summary": lesson_summary,
                        "homework": homework,
                        "areas_to_improve": areas_to_improve
                    }).execute()

                    st.success(
                        "Lesson report saved successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not save lesson report: {e}"
                    )


# =========================================================
# PAYMENTS
# =========================================================

elif page == "Payments":

    st.header("💰 Payments")

    st.write("Manage Boomatt Academy payments.")

    with st.form("payment_form"):

        parent = st.text_input("Parent Name")
        student = st.text_input("Student Name")
        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=500.0
        )

        payment_date = st.date_input(
            "Payment Date"
        )

        status = st.selectbox(
            "Payment Status",
            [
                "Paid",
                "Pending",
                "Partially Paid",
                "Overdue"
            ]
        )

        reference = st.text_input(
            "Payment Reference"
        )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Save Payment"
        )

        if submitted:

            if not parent or not student:
                st.warning(
                    "Please enter the parent and student."
                )

            else:

                try:

                    supabase.table("payments").insert({
                        "parent_name": parent,
                        "student_name": student,
                        "amount": amount,
                        "payment_date": str(payment_date),
                        "status": status,
                        "payment_reference": reference,
                        "notes": notes
                    }).execute()

                    st.success(
                        "Payment saved successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not save payment: {e}"
                    )
