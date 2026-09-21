import streamlit as st
from supabase_client import supabase

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚",
    layout="wide"
)


# =========================
# LOGIN
# =========================

def login():
    st.title("📚 Boomatt Academy")
    st.subheader("Building Confident Learners, One Lesson at a Time")

    st.markdown("### Portal Login")

    email = st.text_input("Email address")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if not email or not password:
            st.error("Please enter your email and password.")
            return

        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if response.user:
                st.session_state.user = response.user
                st.success("Login successful.")
                st.rerun()

        except Exception as e:
            st.error(f"Login failed: {e}")


# =========================
# LOGOUT
# =========================

def logout():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.clear()
    st.rerun()


# =========================
# GET EMAIL
# =========================

def get_current_email():
    if "user" not in st.session_state:
        return None

    user = st.session_state.user

    return user.email


# =========================
# DETERMINE ROLE
# =========================

def get_user_role():

    email = get_current_email()

    if not email:
        return None

    email = email.lower().strip()

    # Academy Director
    if email == "boomattolatunji@gmail.com":
        return "admin"

    # Check tutors table using email
    try:
        result = (
            supabase
            .table("tutors")
            .select("*")
            .eq("email", email)
            .limit(1)
            .execute()
        )

        if result.data:
            return "tutor"

    except Exception as e:
        st.error(f"Could not determine your role: {e}")
        return None

    return "unknown"


# =========================
# ADMIN PORTAL
# =========================

def admin_portal():

    st.sidebar.title("📚 Boomatt Academy")
    st.sidebar.caption("Academy Administrator")

    page = st.sidebar.radio(
        "Admin Menu",
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

    if st.sidebar.button("Logout"):
        logout()

    # -------------------------
    # DASHBOARD
    # -------------------------

    if page == "Dashboard":

        st.title("📊 Admin Dashboard")

        st.success(
            "You are logged in as Academy Administrator."
        )

        col1, col2, col3, col4 = st.columns(4)

        try:
            students = supabase.table("Student").select("id").execute()
            tutors = supabase.table("tutors").select("id").execute()
            parents = supabase.table("parents").select("id").execute()
            timetable = supabase.table("timetable").select("id").execute()

            col1.metric("Students", len(students.data or []))
            col2.metric("Tutors", len(tutors.data or []))
            col3.metric("Parents", len(parents.data or []))
            col4.metric("Timetable Entries", len(timetable.data or []))

        except Exception as e:
            st.error(f"Could not load dashboard: {e}")

    # -------------------------
    # STUDENTS
    # -------------------------

    elif page == "Students":

        st.title("👨‍🎓 Students")

        with st.form("student_form"):

            full_name = st.text_input("Student Name")
            year_grade = st.text_input("Year / Grade")
            school = st.text_input("School")
            subjects = st.text_input("Subjects")

            submitted = st.form_submit_button(
                "Add Student"
            )

            if submitted:

                try:

                    supabase.table("Student").insert({
                        "full_name": full_name,
                        "year_grade": year_grade,
                        "school": school,
                        "subjects": subjects
                    }).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:
                    st.error(f"Could not add student: {e}")

    # -------------------------
    # TUTORS
    # -------------------------

    elif page == "Tutors":

        st.title("👨‍🏫 Tutors")

        with st.form("tutor_form"):

            full_name = st.text_input("Tutor Name")
            email = st.text_input("Tutor Email")
            subjects = st.text_input("Subjects")
            qualification = st.text_input("Qualification")

            submitted = st.form_submit_button(
                "Add Tutor"
            )

            if submitted:

                try:

                    supabase.table("tutors").insert({
                        "full_name": full_name,
                        "email": email.lower().strip(),
                        "subjects": subjects,
                        "qualification": qualification
                    }).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:
                    st.error(f"Could not add tutor: {e}")

    # -------------------------
    # PARENTS
    # -------------------------

    elif page == "Parents":

        st.title("👨‍👩‍👧 Parents")

        with st.form("parent_form"):

            full_name = st.text_input("Parent Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button(
                "Add Parent"
            )

            if submitted:

                try:

                    supabase.table("parents").insert({
                        "full_name": full_name,
                        "email": email,
                        "phone": phone
                    }).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:
                    st.error(f"Could not add parent: {e}")

    # -------------------------
    # TIMETABLE
    # -------------------------

    elif page == "Timetable":

        st.title("📅 Timetable")

        with st.form("timetable_form"):

            student_name = st.text_input("Student Name")
            tutor_name = st.text_input("Tutor Name")
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

            submitted = st.form_submit_button(
                "Add Timetable Entry"
            )

            if submitted:

                try:

                    supabase.table("timetable").insert({
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time,
                        "status": "Scheduled"
                    }).execute()

                    st.success(
                        "Timetable entry added successfully."
                    )

                except Exception as e:
                    st.error(
                        f"Could not add timetable entry: {e}"
                    )

    # -------------------------
    # ATTENDANCE
    # -------------------------

    elif page == "Attendance":

        st.title("📝 Attendance")

        with st.form("attendance_form"):

            student_name = st.text_input("Student Name")
            tutor_name = st.text_input("Tutor Name")
            subject = st.text_input("Subject")
            lesson_date = st.date_input("Lesson Date")

            status = st.selectbox(
                "Attendance",
                [
                    "Present",
                    "Absent",
                    "Late"
                ]
            )

            notes = st.text_area("Notes")

            submitted = st.form_submit_button(
                "Save Attendance"
            )

            if submitted:

                try:

                    supabase.table("attendance").insert({
                        "student_name": student_name,
                        "tutor_name": tutor_name,
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

    # -------------------------
    # LESSON REPORTS
    # -------------------------

    elif page == "Lesson Reports":

        st.title("📖 Lesson Reports")

        with st.form("lesson_report_form"):

            student_name = st.text_input("Student Name")
            tutor_name = st.text_input("Tutor Name")
            subject = st.text_input("Subject")
            lesson_date = st.date_input("Lesson Date")
            topic = st.text_input("Topic")
            lesson_summary = st.text_area("Lesson Summary")
            homework = st.text_area("Homework")
            areas_to_improve = st.text_area(
                "Areas to Improve"
            )

            submitted = st.form_submit_button(
                "Save Lesson Report"
            )

            if submitted:

                try:

                    supabase.table("lesson_reports").insert({
                        "student_name": student_name,
                        "tutor_name": tutor_name,
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

    # -------------------------
    # PAYMENTS
    # -------------------------

    elif page == "Payments":

        st.title("💳 Payments")

        with st.form("payment_form"):

            parent_name = st.text_input("Parent Name")
            student_name = st.text_input("Student Name")
            amount = st.number_input(
                "Amount",
                min_value=0.0,
                step=100.0
            )

            payment_date = st.date_input(
                "Payment Date"
            )

            status = st.selectbox(
                "Payment Status",
                [
                    "Paid",
                    "Pending",
                    "Overdue"
                ]
            )

            payment_reference = st.text_input(
                "Payment Reference"
            )

            notes = st.text_area("Notes")

            submitted = st.form_submit_button(
                "Save Payment"
            )

            if submitted:

                try:

                    supabase.table("payments").insert({
                        "parent_name": parent_name,
                        "student_name": student_name,
                        "amount": amount,
                        "payment_date": str(payment_date),
                        "status": status,
                        "payment_reference": payment_reference,
                        "notes": notes
                    }).execute()

                    st.success(
                        "Payment saved successfully."
                    )

                except Exception as e:
                    st.error(
                        f"Could not save payment: {e}"
                    )


# =========================
# TUTOR PORTAL
# =========================

def tutor_portal():

    email = get_current_email()

    st.sidebar.title("📚 Boomatt Academy")
    st.sidebar.caption("Tutor Portal")

    if st.sidebar.button("Logout"):
        logout()

    try:

        tutor_result = (
            supabase
            .table("tutors")
            .select("*")
            .eq("email", email.lower().strip())
            .limit(1)
            .execute()
        )

        if not tutor_result.data:

            st.error(
                "Your tutor profile could not be found."
            )
            return

        tutor = tutor_result.data[0]

        tutor_name = tutor.get("full_name", "")

    except Exception as e:

        st.error(
            f"Could not load tutor profile: {e}"
        )
        return

    menu = st.sidebar.radio(
        "Tutor Menu",
        [
            "Dashboard",
            "My Students",
            "My Timetable",
            "Attendance",
            "Lesson Reports"
        ]
    )

    # -------------------------
    # TUTOR DASHBOARD
    # -------------------------

    if menu == "Dashboard":

        st.title("👨‍🏫 Tutor Dashboard")

        st.success(
            f"Welcome, {tutor_name}."
        )

        st.write(
            "You are logged in to the Boomatt Academy Tutor Portal."
        )

        st.info(
            f"Registered email: {email}"
        )

    # -------------------------
    # MY STUDENTS
    # -------------------------

    elif menu == "My Students":

        st.title("👨‍🎓 My Students")

        try:

            result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            if result.data:

                students = []

                for item in result.data:

                    if item.get("student_name") not in students:
                        students.append(
                            item.get("student_name")
                        )

                for student in students:
                    st.write(f"• {student}")

            else:

                st.info(
                    "No students have been assigned to you yet."
                )

        except Exception as e:

            st.error(
                f"Could not load students: {e}"
            )

    # -------------------------
    # MY TIMETABLE
    # -------------------------

    elif menu == "My Timetable":

        st.title("📅 My Timetable")

        try:

            result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            if result.data:
                st.dataframe(
                    result.data,
                    use_container_width=True
                )
            else:
                st.info(
                    "No timetable entries assigned to you."
                )

        except Exception as e:

            st.error(
                f"Could not load timetable: {e}"
            )

    # -------------------------
    # ATTENDANCE
    # -------------------------

    elif menu == "Attendance":

        st.title("📝 Attendance")

        with st.form("tutor_attendance_form"):

            student_name = st.text_input(
                "Student Name"
            )

            subject = st.text_input(
                "Subject"
            )

            lesson_date = st.date_input(
                "Lesson Date"
            )

            status = st.selectbox(
                "Attendance",
                [
                    "Present",
                    "Absent",
                    "Late"
                ]
            )

            notes = st.text_area(
                "Notes"
            )

            submitted = st.form_submit_button(
                "Save Attendance"
            )

            if submitted:

                try:

                    supabase.table("attendance").insert({
                        "student_name": student_name,
                        "tutor_name": tutor_name,
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

    # -------------------------
    # LESSON REPORTS
    # -------------------------

    elif menu == "Lesson Reports":

        st.title("📖 Lesson Reports")

        with st.form("tutor_report_form"):

            student_name = st.text_input(
                "Student Name"
            )

            subject = st.text_input(
                "Subject"
            )

            lesson_date = st.date_input(
                "Lesson Date"
            )

            topic = st.text_input(
                "Topic"
            )

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
                "Submit Lesson Report"
            )

            if submitted:

                try:

                    supabase.table("lesson_reports").insert({
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "topic": topic,
                        "lesson_summary": lesson_summary,
                        "homework": homework,
                        "areas_to_improve": areas_to_improve
                    }).execute()

                    st.success(
                        "Lesson report submitted successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not submit lesson report: {e}"
                    )


# =========================
# MAIN
# =========================

if "user" not in st.session_state:

    login()

else:

    role = get_user_role()

    if role == "admin":

        admin_portal()

    elif role == "tutor":

        tutor_portal()

    elif role == "unknown":

        st.title("📚 Boomatt Academy")

        st.error(
            "Your account has not been assigned a portal role yet."
        )

        st.write(
            f"Logged in as: {get_current_email()}"
        )

    else:

        st.error(
            "We could not determine your portal role."
        )
