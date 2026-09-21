import streamlit as st
from supabase_client import supabase
from datetime import date


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Boomatt Academy Portal",
    page_icon="📚",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "user" not in st.session_state:
    st.session_state.user = None


# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():

    st.title("📚 Boomatt Academy")
    st.subheader("Building Confident Learners, One Lesson at a Time")

    st.write("Please sign in to access your portal.")

    with st.form("login_form"):

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Sign In")

        if submitted:

            if not email or not password:
                st.error("Please enter your email and password.")
                return

            try:

                response = supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })

                st.session_state.user = response.user

                st.success("Login successful.")
                st.rerun()

            except Exception as e:

                st.error(f"Login failed: {e}")


# =========================================================
# LOGOUT
# =========================================================

def logout():

    try:
        supabase.auth.sign_out()
    except:
        pass

    st.session_state.user = None
    st.rerun()


# =========================================================
# GET CURRENT USER
# =========================================================

def get_current_email():

    if st.session_state.user:
        return st.session_state.user.email

    return None


# =========================================================
# DETERMINE ROLE
# =========================================================

def get_user_role():

    email = get_current_email()

    if not email:
        return None

    # Academy Director / Admin
    if email.lower() == "boomattolatunji@gmail.com":
        return "admin"

    # Check whether the logged-in user belongs to a tutor
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

    except:
        pass

    return "unknown"


# =========================================================
# ADMIN DASHBOARD
# =========================================================

def admin_dashboard():

    st.title("🏫 Boomatt Academy — Admin Portal")

    st.success(
        f"You are logged in as Academy Administrator: {get_current_email()}"
    )

    if st.button("Logout"):
        logout()

    st.divider()

    menu = st.sidebar.radio(
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

    # =====================================================
    # DASHBOARD
    # =====================================================

    if menu == "Dashboard":

        st.header("📊 Dashboard")

        try:
            students = supabase.table("Student").select("id").execute()
            tutors = supabase.table("tutors").select("id").execute()
            parents = supabase.table("parents").select("id").execute()
            timetable = supabase.table("timetable").select("id").execute()

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Students", len(students.data))
            col2.metric("Tutors", len(tutors.data))
            col3.metric("Parents", len(parents.data))
            col4.metric("Timetable Entries", len(timetable.data))

        except Exception as e:

            st.error(f"Could not load dashboard: {e}")

    # =====================================================
    # STUDENTS
    # =====================================================

    elif menu == "Students":

        st.header("👨‍🎓 Students")

        with st.form("student_form"):

            name = st.text_input("Full Name")
            year_grade = st.text_input("Year / Grade")
            school = st.text_input("School")
            subjects = st.text_input("Subjects")

            submitted = st.form_submit_button("Add Student")

            if submitted:

                try:

                    supabase.table("Student").insert({
                        "full_name": name,
                        "year_grade": year_grade,
                        "school": school,
                        "subjects": subjects
                    }).execute()

                    st.success(f"{name} has been added successfully.")

                except Exception as e:

                    st.error(f"Could not add student: {e}")

        st.divider()

        try:

            result = (
                supabase
                .table("Student")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(result.data, use_container_width=True)
            else:
                st.info("No students found.")

        except Exception as e:

            st.error(f"Could not load students: {e}")

    # =====================================================
    # TUTORS
    # =====================================================

    elif menu == "Tutors":

        st.header("👩‍🏫 Tutors")

        with st.form("tutor_form"):

            name = st.text_input("Full Name")
            email = st.text_input("Email")
            subjects = st.text_input("Subjects")
            qualification = st.text_input("Qualification")

            submitted = st.form_submit_button("Add Tutor")

            if submitted:

                try:

                    supabase.table("tutors").insert({
                        "full_name": name,
                        "email": email,
                        "subjects": subjects,
                        "qualification": qualification
                    }).execute()

                    st.success(f"{name} has been added successfully.")

                except Exception as e:

                    st.error(f"Could not add tutor: {e}")

        st.divider()

        try:

            result = (
                supabase
                .table("tutors")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(result.data, use_container_width=True)
            else:
                st.info("No tutors found.")

        except Exception as e:

            st.error(f"Could not load tutors: {e}")

    # =====================================================
    # PARENTS
    # =====================================================

    elif menu == "Parents":

        st.header("👨‍👩‍👧 Parents")

        with st.form("parent_form"):

            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button("Add Parent")

            if submitted:

                try:

                    supabase.table("parents").insert({
                        "full_name": name,
                        "email": email,
                        "phone": phone
                    }).execute()

                    st.success(f"{name} has been added successfully.")

                except Exception as e:

                    st.error(f"Could not add parent: {e}")

        st.divider()

        try:

            result = (
                supabase
                .table("parents")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(result.data, use_container_width=True)
            else:
                st.info("No parents found.")

        except Exception as e:

            st.error(f"Could not load parents: {e}")

    # =====================================================
    # TIMETABLE
    # =====================================================

    elif menu == "Timetable":

        st.header("📅 Timetable")

        with st.form("timetable_form"):

            student_name = st.text_input("Student")
            tutor_name = st.text_input("Tutor")
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
                ["Scheduled", "Completed", "Cancelled"]
            )

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
                        "status": status
                    }).execute()

                    st.success("Timetable entry added successfully.")

                except Exception as e:

                    st.error(f"Could not add timetable entry: {e}")

        st.divider()

        try:

            result = (
                supabase
                .table("timetable")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(result.data, use_container_width=True)
            else:
                st.info("No timetable entries found.")

        except Exception as e:

            st.error(f"Could not load timetable: {e}")

    # =====================================================
    # ATTENDANCE
    # =====================================================

    elif menu == "Attendance":

        st.header("✅ Attendance")

        with st.form("attendance_form"):

            student_name = st.text_input("Student")
            tutor_name = st.text_input("Tutor")
            subject = st.text_input("Subject")
            lesson_date = st.date_input("Lesson Date", date.today())

            status = st.selectbox(
                "Attendance Status",
                ["Present", "Absent", "Late", "Excused"]
            )

            notes = st.text_area("Notes")

            submitted = st.form_submit_button(
                "Add Attendance"
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

                    st.success("Attendance saved successfully.")

                except Exception as e:

                    st.error(f"Could not save attendance: {e}")

        st.divider()

        try:

            result = (
                supabase
                .table("attendance")
                .select("*")
                .order("lesson_date", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(result.data, use_container_width=True)
            else:
                st.info("No attendance records found.")

        except Exception as e:

            st.error(f"Could not load attendance: {e}")

    # =====================================================
    # LESSON REPORTS
    # =====================================================

    elif menu == "Lesson Reports":

        st.header("📝 Lesson Reports")

        with st.form("lesson_report_form"):

            student_name = st.text_input("Student")
            tutor_name = st.text_input("Tutor")
            subject = st.text_input("Subject")
            lesson_date = st.date_input(
                "Lesson Date",
                date.today()
            )

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

        st.divider()

        try:

            result = (
                supabase
                .table("lesson_reports")
                .select("*")
                .order("lesson_date", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(
                    result.data,
                    use_container_width=True
                )
            else:
                st.info("No lesson reports found.")

        except Exception as e:

            st.error(
                f"Could not load lesson reports: {e}"
            )

    # =====================================================
    # PAYMENTS
    # =====================================================

    elif menu == "Payments":

        st.header("💳 Payments")

        with st.form("payment_form"):

            parent_name = st.text_input("Parent")
            student_name = st.text_input("Student")
            amount = st.number_input(
                "Amount",
                min_value=0.0,
                step=500.0
            )

            payment_date = st.date_input(
                "Payment Date",
                date.today()
            )

            status = st.selectbox(
                "Payment Status",
                ["Paid", "Pending", "Overdue"]
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

        st.divider()

        try:

            result = (
                supabase
                .table("payments")
                .select("*")
                .order("payment_date", desc=True)
                .execute()
            )

            if result.data:
                st.dataframe(
                    result.data,
                    use_container_width=True
                )
            else:
                st.info("No payment records found.")

        except Exception as e:

            st.error(
                f"Could not load payments: {e}"
            )


# =========================================================
# TUTOR PORTAL
# =========================================================

def tutor_dashboard():

    email = get_current_email()

    # Find tutor information
    try:

        tutor_result = (
            supabase
            .table("tutors")
            .select("*")
            .eq("email", email)
            .limit(1)
            .execute()
        )

    except Exception as e:

        st.error(f"Could not load tutor profile: {e}")
        return

    if not tutor_result.data:

        st.error(
            "Your tutor account has not been connected to a tutor profile."
        )
        return

    tutor = tutor_result.data[0]

    tutor_name = tutor.get("full_name", "Tutor")

    st.title(f"👩‍🏫 Tutor Portal")

    st.success(
        f"Welcome, {tutor_name}."
    )

    if st.button("Logout"):
        logout()

    st.divider()

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

    # =====================================================
    # TUTOR DASHBOARD
    # =====================================================

    if menu == "Dashboard":

        st.header("🏠 My Dashboard")

        st.write(
            f"**Tutor:** {tutor_name}"
        )

        st.write(
            f"**Email:** {email}"
        )

        st.write(
            f"**Subjects:** {tutor.get('subjects', '')}"
        )

        st.write(
            f"**Qualification:** {tutor.get('qualification', '')}"
        )

        st.divider()

        try:

            timetable_result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            attendance_result = (
                supabase
                .table("attendance")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            reports_result = (
                supabase
                .table("lesson_reports")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "My Lessons",
                len(timetable_result.data)
            )

            col2.metric(
                "Attendance Records",
                len(attendance_result.data)
            )

            col3.metric(
                "Lesson Reports",
                len(reports_result.data)
            )

        except Exception as e:

            st.error(
                f"Could not load tutor dashboard: {e}"
            )

    # =====================================================
    # MY STUDENTS
    # =====================================================

    elif menu == "My Students":

        st.header("👨‍🎓 My Students")

        try:

            timetable_result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            if not timetable_result.data:

                st.info(
                    "You currently have no students assigned."
                )

            else:

                student_names = sorted(
                    list(
                        set(
                            row["student_name"]
                            for row in timetable_result.data
                            if row.get("student_name")
                        )
                    )
                )

                for student_name in student_names:

                    st.subheader(
                        f"👤 {student_name}"
                    )

                    try:

                        student_result = (
                            supabase
                            .table("Student")
                            .select("*")
                            .eq("full_name", student_name)
                            .limit(1)
                            .execute()
                        )

                        if student_result.data:

                            student = student_result.data[0]

                            col1, col2 = st.columns(2)

                            col1.write(
                                f"**Year / Grade:** {student.get('year_grade', '')}"
                            )

                            col2.write(
                                f"**School:** {student.get('school', '')}"
                            )

                            st.write(
                                f"**Subjects:** {student.get('subjects', '')}"
                            )

                        else:

                            st.info(
                                "Student profile details not found."
                            )

                    except Exception as e:

                        st.error(
                            f"Could not load student details: {e}"
                        )

                    st.divider()

        except Exception as e:

            st.error(
                f"Could not load your students: {e}"
            )

    # =====================================================
    # MY TIMETABLE
    # =====================================================

    elif menu == "My Timetable":

        st.header("📅 My Timetable")

        try:

            result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .order("created_at", desc=True)
                .execute()
            )

            if result.data:

                st.dataframe(
                    result.data,
                    use_container_width=True
                )

            else:

                st.info(
                    "You currently have no timetable entries."
                )

        except Exception as e:

            st.error(
                f"Could not load your timetable: {e}"
            )

    # =====================================================
    # TUTOR ATTENDANCE
    # =====================================================

    elif menu == "Attendance":

        st.header("✅ Attendance")

        try:

            timetable_result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            if timetable_result.data:

                student_options = sorted(
                    list(
                        set(
                            row["student_name"]
                            for row in timetable_result.data
                            if row.get("student_name")
                        )
                    )
                )

                subject_options = sorted(
                    list(
                        set(
                            row["subject"]
                            for row in timetable_result.data
                            if row.get("subject")
                        )
                    )
                )

            else:

                student_options = []
                subject_options = []

        except:

            student_options = []
            subject_options = []

        if not student_options:

            st.info(
                "No students have been assigned to you yet."
            )

        else:

            with st.form("tutor_attendance_form"):

                student_name = st.selectbox(
                    "Student",
                    student_options
                )

                subject = st.selectbox(
                    "Subject",
                    subject_options
                    if subject_options
                    else ["English"]
                )

                lesson_date = st.date_input(
                    "Lesson Date",
                    date.today()
                )

                status = st.selectbox(
                    "Attendance Status",
                    [
                        "Present",
                        "Absent",
                        "Late",
                        "Excused"
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

        st.divider()

        st.subheader("My Attendance Records")

        try:

            result = (
                supabase
                .table("attendance")
                .select("*")
                .eq("tutor_name", tutor_name)
                .order("lesson_date", desc=True)
                .execute()
            )

            if result.data:

                st.dataframe(
                    result.data,
                    use_container_width=True
                )

            else:

                st.info(
                    "No attendance records yet."
                )

        except Exception as e:

            st.error(
                f"Could not load attendance: {e}"
            )

    # =====================================================
    # TUTOR LESSON REPORTS
    # =====================================================

    elif menu == "Lesson Reports":

        st.header("📝 Lesson Reports")

        try:

            timetable_result = (
                supabase
                .table("timetable")
                .select("*")
                .eq("tutor_name", tutor_name)
                .execute()
            )

            if timetable_result.data:

                student_options = sorted(
                    list(
                        set(
                            row["student_name"]
                            for row in timetable_result.data
                            if row.get("student_name")
                        )
                    )
                )

                subject_options = sorted(
                    list(
                        set(
                            row["subject"]
                            for row in timetable_result.data
                            if row.get("subject")
                        )
                    )
                )

            else:

                student_options = []
                subject_options = []

        except:

            student_options = []
            subject_options = []

        if not student_options:

            st.info(
                "No students have been assigned to you yet."
            )

        else:

            with st.form("tutor_report_form"):

                student_name = st.selectbox(
                    "Student",
                    student_options
                )

                subject = st.selectbox(
                    "Subject",
                    subject_options
                    if subject_options
                    else ["English"]
                )

                lesson_date = st.date_input(
                    "Lesson Date",
                    date.today()
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
                    "Save Lesson Report"
                )

                if submitted:

                    try:

                        supabase.table(
                            "lesson_reports"
                        ).insert({
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

        st.divider()

        st.subheader("My Previous Lesson Reports")

        try:

            result = (
                supabase
                .table("lesson_reports")
                .select("*")
                .eq("tutor_name", tutor_name)
                .order("lesson_date", desc=True)
                .execute()
            )

            if result.data:

                st.dataframe(
                    result.data,
                    use_container_width=True
                )

            else:

                st.info(
                    "No lesson reports yet."
                )

        except Exception as e:

            st.error(
                f"Could not load lesson reports: {e}"
            )


# =========================================================
# MAIN APPLICATION
# =========================================================

if st.session_state.user is None:

    login_page()

else:

    role = get_user_role()

    if role == "admin":

        admin_dashboard()

    elif role == "tutor":

        tutor_dashboard()

    else:

        st.error(
            "Your account has not been assigned a portal role yet."
        )

        st.write(
            f"Logged in as: {get_current_email()}"
        )

        if st.button("Logout"):
            logout()
