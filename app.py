import streamlit as st
from supabase_client import supabase
from datetime import date


# ============================================================
# BOOMATT ACADEMY
# MASTER PORTAL
# ============================================================

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# GLOBAL DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* Page */
    .stApp {
        background: #F6F8FC;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #102A43;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    /* Typography */
    h1, h2, h3, h4 {
        color: #102A43 !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 40px;
    }

    /* Forms */
    [data-testid="stForm"] {
        background: #FFFFFF;
        border: 1px solid #E3E8EF;
        border-radius: 14px;
        padding: 22px;
    }

    /* Footer */
    .boomatt-footer {
        text-align: center;
        color: #829AB1;
        font-size: 12px;
        margin-top: 40px;
        padding: 20px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def current_email():
    if "user" not in st.session_state:
        return None
    return st.session_state.user.email


def logout():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.clear()
    st.rerun()


def footer():
    st.markdown(
        """
        <div class="boomatt-footer">
            © 2026 Boomatt Academy · Building Confident Learners, One Lesson at a Time
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LOGIN
# ============================================================

def login():

    st.write("")
    st.write("")
    st.write("")

    left, centre, right = st.columns([1, 2, 1])

    with centre:

        st.markdown(
            "<h1 style='text-align:center;'>📚</h1>",
            unsafe_allow_html=True
        )

        st.title("Boomatt Academy")

        st.markdown(
            "<p style='text-align:center;'>Building Confident Learners, One Lesson at a Time</p>",
            unsafe_allow_html=True
        )

        st.divider()

        st.subheader("Sign in")

        email = st.text_input(
            "Email address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        if st.button(
            "Sign in to portal",
            type="primary",
            use_container_width=True
        ):

            if not email or not password:

                st.warning(
                    "Please enter your email address and password."
                )

                return

            try:

                response = supabase.auth.sign_in_with_password(
                    {
                        "email": email.strip().lower(),
                        "password": password
                    }
                )

                if response.user:

                    st.session_state.user = response.user
                    st.rerun()

            except Exception as e:

                st.error(
                    "Login failed. Please check your email and password."
                )

                st.caption(str(e))

    footer()


# ============================================================
# ROLE DETECTION
# ============================================================

def get_role():

    email = current_email()

    if not email:
        return None

    email = email.lower().strip()

    # Academy Director
    if email == "boomattolatunji@gmail.com":
        return "admin"

    # Existing test tutor
    if email == "test@gmail.com":
        return "tutor"

    # Registered tutors
    try:

        result = (
            supabase
            .table("tutors")
            .select("id")
            .eq("email", email)
            .limit(1)
            .execute()
        )

        if result.data:
            return "tutor"

    except Exception:
        pass

    return "unknown"


# ============================================================
# ADMIN SIDEBAR
# ============================================================

def admin_sidebar():

    st.sidebar.title("📚 Boomatt")

    st.sidebar.caption(
        "Boomatt Academy"
    )

    st.sidebar.caption(
        "Building Confident Learners, One Lesson at a Time"
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "ACADEMY ADMINISTRATOR"
    )

    page = st.sidebar.radio(
        "Workspace",
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

    st.sidebar.divider()

    st.sidebar.caption(
        current_email()
    )

    if st.sidebar.button(
        "Log out",
        use_container_width=True
    ):
        logout()

    return page


# ============================================================
# ADMIN DASHBOARD
# ============================================================

def admin_dashboard():

    st.title("Welcome back, Academy Director 👋")

    st.write(
        "Your central workspace for managing learners, tutors, lessons and academy operations."
    )

    st.divider()

    # --------------------------------------------------------
    # COUNTS
    # --------------------------------------------------------

    try:

        students = (
            supabase
            .table("Student")
            .select("id")
            .execute()
        )

        tutors = (
            supabase
            .table("tutors")
            .select("id")
            .execute()
        )

        parents = (
            supabase
            .table("parents")
            .select("id")
            .execute()
        )

        timetable = (
            supabase
            .table("timetable")
            .select("id")
            .execute()
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Students",
                len(students.data or [])
            )

        with c2:
            st.metric(
                "Tutors",
                len(tutors.data or [])
            )

        with c3:
            st.metric(
                "Parents",
                len(parents.data or [])
            )

        with c4:
            st.metric(
                "Scheduled lessons",
                len(timetable.data or [])
            )

    except Exception as e:

        st.error(
            f"Dashboard could not load completely: {e}"
        )

    # --------------------------------------------------------
    # QUICK ACCESS
    # --------------------------------------------------------

    st.subheader("Quick access")

    q1, q2, q3, q4 = st.columns(4)

    with q1:
        st.info(
            "👨‍🎓 **Students**\n\n"
            "Create and manage learner records."
        )

    with q2:
        st.info(
            "👨‍🏫 **Tutors**\n\n"
            "Manage your teaching team."
        )

    with q3:
        st.info(
            "📅 **Timetable**\n\n"
            "Organise lessons and schedules."
        )

    with q4:
        st.info(
            "📖 **Reports**\n\n"
            "Monitor teaching and learning."
        )

    # --------------------------------------------------------
    # TIMETABLE
    # --------------------------------------------------------

    st.subheader("Recent timetable")

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .order("created_at", desc=True)
            .limit(10)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "Your timetable is currently empty."
            )

    except Exception as e:

        st.error(
            f"Could not load timetable: {e}"
        )

    # --------------------------------------------------------
    # RECENT REPORTS
    # --------------------------------------------------------

    st.subheader("Recent lesson reports")

    try:

        result = (
            supabase
            .table("lesson_reports")
            .select("*")
            .order("lesson_date", desc=True)
            .limit(5)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No lesson reports have been submitted yet."
            )

    except Exception as e:

        st.error(
            f"Could not load lesson reports: {e}"
        )


# ============================================================
# STUDENTS
# ============================================================

def admin_students():

    st.title("Students")

    st.caption(
        "Create and manage learner profiles."
    )

    with st.form("student_form"):

        st.subheader("Add learner")

        full_name = st.text_input(
            "Student name"
        )

        year_grade = st.text_input(
            "Year / Grade"
        )

        school = st.text_input(
            "School"
        )

        subjects = st.text_input(
            "Subjects"
        )

        submitted = st.form_submit_button(
            "Add student",
            type="primary"
        )

        if submitted:

            if not full_name:

                st.warning(
                    "Please enter the student's name."
                )

            else:

                try:

                    supabase.table("Student").insert(
                        {
                            "full_name": full_name,
                            "year_grade": year_grade,
                            "school": school,
                            "subjects": subjects
                        }
                    ).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add student: {e}"
                    )

    st.subheader("Learner records")

    try:

        result = (
            supabase
            .table("Student")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No students have been added yet."
            )

    except Exception as e:

        st.error(
            f"Could not load students: {e}"
        )


# ============================================================
# TUTORS
# ============================================================

def admin_tutors():

    st.title("Tutors")

    st.caption(
        "Manage the Boomatt Academy teaching team."
    )

    with st.form("tutor_form"):

        st.subheader("Add tutor")

        full_name = st.text_input(
            "Tutor name"
        )

        email = st.text_input(
            "Tutor email"
        )

        subjects = st.text_input(
            "Subjects"
        )

        qualification = st.text_input(
            "Qualification"
        )

        submitted = st.form_submit_button(
            "Add tutor",
            type="primary"
        )

        if submitted:

            if not full_name or not email:

                st.warning(
                    "Tutor name and email are required."
                )

            else:

                try:

                    supabase.table("tutors").insert(
                        {
                            "full_name": full_name,
                            "email": email.strip().lower(),
                            "subjects": subjects,
                            "qualification": qualification
                        }
                    ).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add tutor: {e}"
                    )

    st.subheader("Teaching team")

    try:

        result = (
            supabase
            .table("tutors")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No tutors have been added yet."
            )

    except Exception as e:

        st.error(
            f"Could not load tutors: {e}"
        )


# ============================================================
# PARENTS
# ============================================================

def admin_parents():

    st.title("Parents")

    st.caption(
        "Manage parent and guardian records."
    )

    with st.form("parent_form"):

        st.subheader("Add parent")

        full_name = st.text_input(
            "Parent name"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone"
        )

        submitted = st.form_submit_button(
            "Add parent",
            type="primary"
        )

        if submitted:

            if not full_name:

                st.warning(
                    "Please enter the parent's name."
                )

            else:

                try:

                    supabase.table("parents").insert(
                        {
                            "full_name": full_name,
                            "email": email,
                            "phone": phone
                        }
                    ).execute()

                    st.success(
                        f"{full_name} has been added successfully."
                    )

                except Exception as e:

                    st.error(
                        f"Could not add parent: {e}"
                    )

    st.subheader("Parent records")

    try:

        result = (
            supabase
            .table("parents")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No parents have been added yet."
            )

    except Exception as e:

        st.error(
            f"Could not load parents: {e}"
        )


# ============================================================
# TIMETABLE
# ============================================================

def admin_timetable():

    st.title("Timetable")

    st.caption(
        "Create and manage academy lesson schedules."
    )

    with st.form("timetable_form"):

        st.subheader("Schedule a lesson")

        student_name = st.text_input(
            "Student name"
        )

        tutor_name = st.text_input(
            "Tutor name"
        )

        subject = st.text_input(
            "Subject"
        )

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

        c1, c2 = st.columns(2)

        with c1:

            start_time = st.text_input(
                "Start time",
                placeholder="6:00 PM"
            )

        with c2:

            end_time = st.text_input(
                "End time",
                placeholder="7:00 PM"
            )

        status = st.selectbox(
            "Status",
            [
                "Scheduled",
                "Completed",
                "Cancelled",
                "Rescheduled"
            ]
        )

        submitted = st.form_submit_button(
            "Add lesson",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("timetable").insert(
                    {
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time,
                        "status": status
                    }
                ).execute()

                st.success(
                    "Lesson has been added to the timetable."
                )

            except Exception as e:

                st.error(
                    f"Could not add lesson: {e}"
                )

    st.subheader("Academy timetable")

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No lessons have been scheduled yet."
            )

    except Exception as e:

        st.error(
            f"Could not load timetable: {e}"
        )


# ============================================================
# ATTENDANCE
# ============================================================

def admin_attendance():

    st.title("Attendance")

    st.caption(
        "Record and review learner attendance."
    )

    with st.form("attendance_form"):

        st.subheader("Record attendance")

        student_name = st.text_input(
            "Student name"
        )

        tutor_name = st.text_input(
            "Tutor name"
        )

        subject = st.text_input(
            "Subject"
        )

        lesson_date = st.date_input(
            "Lesson date",
            value=date.today()
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
            "Save attendance",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("attendance").insert(
                    {
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "status": status,
                        "notes": notes
                    }
                ).execute()

                st.success(
                    "Attendance saved successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not save attendance: {e}"
                )

    st.subheader("Attendance records")

    try:

        result = (
            supabase
            .table("attendance")
            .select("*")
            .order("lesson_date", desc=True)
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No attendance records yet."
            )

    except Exception as e:

        st.error(
            f"Could not load attendance: {e}"
        )


# ============================================================
# LESSON REPORTS
# ============================================================

def admin_reports():

    st.title("Lesson Reports")

    st.caption(
        "Monitor lesson delivery, progress and homework."
    )

    with st.form("lesson_report_form"):

        st.subheader("Create lesson report")

        student_name = st.text_input(
            "Student name"
        )

        tutor_name = st.text_input(
            "Tutor name"
        )

        subject = st.text_input(
            "Subject"
        )

        lesson_date = st.date_input(
            "Lesson date",
            value=date.today()
        )

        topic = st.text_input(
            "Topic"
        )

        lesson_summary = st.text_area(
            "Lesson summary"
        )

        homework = st.text_area(
            "Homework"
        )

        areas_to_improve = st.text_area(
            "Areas to improve"
        )

        submitted = st.form_submit_button(
            "Save lesson report",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("lesson_reports").insert(
                    {
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "topic": topic,
                        "lesson_summary": lesson_summary,
                        "homework": homework,
                        "areas_to_improve": areas_to_improve
                    }
                ).execute()

                st.success(
                    "Lesson report saved successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not save lesson report: {e}"
                )

    st.subheader("Lesson reports")

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No lesson reports yet."
            )

    except Exception as e:

        st.error(
            f"Could not load lesson reports: {e}"
        )


# ============================================================
# PAYMENTS
# ============================================================

def admin_payments():

    st.title("Payments")

    st.caption(
        "Track academy payment records."
    )

    with st.form("payment_form"):

        st.subheader("Record payment")

        parent_name = st.text_input(
            "Parent name"
        )

        student_name = st.text_input(
            "Student name"
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=500.0
        )

        payment_date = st.date_input(
            "Payment date",
            value=date.today()
        )

        status = st.selectbox(
            "Payment status",
            [
                "Paid",
                "Pending",
                "Overdue"
            ]
        )

        payment_reference = st.text_input(
            "Payment reference"
        )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Save payment",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("payments").insert(
                    {
                        "parent_name": parent_name,
                        "student_name": student_name,
                        "amount": amount,
                        "payment_date": str(payment_date),
                        "status": status,
                        "payment_reference": payment_reference,
                        "notes": notes
                    }
                ).execute()

                st.success(
                    "Payment saved successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not save payment: {e}"
                )

    st.subheader("Payment records")

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No payment records yet."
            )

    except Exception as e:

        st.error(
            f"Could not load payments: {e}"
        )


# ============================================================
# ADMIN PORTAL
# ============================================================

def admin_portal():

    page = admin_sidebar()

    if page == "Dashboard":
        admin_dashboard()

    elif page == "Students":
        admin_students()

    elif page == "Tutors":
        admin_tutors()

    elif page == "Parents":
        admin_parents()

    elif page == "Timetable":
        admin_timetable()

    elif page == "Attendance":
        admin_attendance()

    elif page == "Lesson Reports":
        admin_reports()

    elif page == "Payments":
        admin_payments()

    footer()


# ============================================================
# TUTOR SIDEBAR
# ============================================================

def tutor_sidebar():

    st.sidebar.title("📚 Boomatt")

    st.sidebar.caption(
        "Boomatt Academy"
    )

    st.sidebar.caption(
        "Building Confident Learners, One Lesson at a Time"
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "TUTOR PORTAL"
    )

    page = st.sidebar.radio(
        "Workspace",
        [
            "Dashboard",
            "My Students",
            "My Timetable",
            "Attendance",
            "Lesson Reports"
        ]
    )

    st.sidebar.divider()

    st.sidebar.caption(
        current_email()
    )

    if st.sidebar.button(
        "Log out",
        use_container_width=True
    ):
        logout()

    return page


# ============================================================
# TUTOR PROFILE
# ============================================================

def tutor_profile():

    email = current_email()

    if not email:
        return None

    try:

        result = (
            supabase
            .table("tutors")
            .select("*")
            .eq("email", email.lower().strip())
            .limit(1)
            .execute()
        )

        if result.data:
            return result.data[0]

    except Exception as e:

        st.error(
            f"Could not load tutor profile: {e}"
        )

    return None


# ============================================================
# TUTOR DASHBOARD
# ============================================================

def tutor_dashboard(tutor):

    tutor_name = tutor.get(
        "full_name",
        "Tutor"
    )

    st.title(
        f"Welcome, {tutor_name} 👋"
    )

    st.write(
        "Your Boomatt Academy teaching workspace."
    )

    st.divider()

    try:

        timetable = (
            supabase
            .table("timetable")
            .select("*")
            .eq("tutor_name", tutor_name)
            .execute()
        )

        students = {
            item.get("student_name")
            for item in (timetable.data or [])
            if item.get("student_name")
        }

        reports = (
            supabase
            .table("lesson_reports")
            .select("id")
            .eq("tutor_name", tutor_name)
            .execute()
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "My Students",
                len(students)
            )

        with c2:
            st.metric(
                "My Lessons",
                len(timetable.data or [])
            )

        with c3:
            st.metric(
                "Lesson Reports",
                len(reports.data or [])
            )

    except Exception as e:

        st.error(
            f"Could not load tutor dashboard: {e}"
        )

    st.subheader("My timetable")

    try:

        if timetable.data:

            st.dataframe(
                timetable.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No lessons have been assigned to you yet."
            )

    except Exception:
        pass


# ============================================================
# TUTOR STUDENTS
# ============================================================

def tutor_students(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("My Students")

    st.caption(
        "Learners currently assigned to you."
    )

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .eq("tutor_name", tutor_name)
            .execute()
        )

        students = sorted(
            {
                item.get("student_name")
                for item in (result.data or [])
                if item.get("student_name")
            }
        )

        if not students:

            st.info(
                "No students have been assigned to you yet."
            )

            return

        for student in students:

            st.subheader(student)

            try:

                info = (
                    supabase
                    .table("Student")
                    .select("*")
                    .eq("full_name", student)
                    .limit(1)
                    .execute()
                )

                if info.data:

                    data = info.data[0]

                    c1, c2, c3 = st.columns(3)

                    with c1:
                        st.write("**Year / Grade**")
                        st.write(
                            data.get("year_grade", "")
                        )

                    with c2:
                        st.write("**School**")
                        st.write(
                            data.get("school", "")
                        )

                    with c3:
                        st.write("**Subjects**")
                        st.write(
                            data.get("subjects", "")
                        )

            except Exception:
                pass

            st.divider()

    except Exception as e:

        st.error(
            f"Could not load your students: {e}"
        )


# ============================================================
# TUTOR TIMETABLE
# ============================================================

def tutor_timetable(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("My Timetable")

    st.caption(
        "Your assigned teaching schedule."
    )

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .eq("tutor_name", tutor_name)
            .order("created_at")
            .execute()
        )

        if result.data:

            st.dataframe(
                result.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No timetable entries have been assigned to you."
            )

    except Exception as e:

        st.error(
            f"Could not load your timetable: {e}"
        )


# ============================================================
# TUTOR ATTENDANCE
# ============================================================

def tutor_attendance(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("Attendance")

    st.caption(
        "Record attendance for your lessons."
    )

    with st.form("tutor_attendance_form"):

        student_name = st.text_input(
            "Student name"
        )

        subject = st.text_input(
            "Subject"
        )

        lesson_date = st.date_input(
            "Lesson date",
            value=date.today()
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
            "Save attendance",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("attendance").insert(
                    {
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "status": status,
                        "notes": notes
                    }
                ).execute()

                st.success(
                    "Attendance saved successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not save attendance: {e}"
                )


# ============================================================
# TUTOR REPORTS
# ============================================================

def tutor_reports(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("Lesson Reports")

    st.caption(
        "Record lesson progress, homework and areas for improvement."
    )

    with st.form("tutor_report_form"):

        student_name = st.text_input(
            "Student name"
        )

        subject = st.text_input(
            "Subject"
        )

        lesson_date = st.date_input(
            "Lesson date",
            value=date.today()
        )

        topic = st.text_input(
            "Topic"
        )

        lesson_summary = st.text_area(
            "Lesson summary"
        )

        homework = st.text_area(
            "Homework"
        )

        areas_to_improve = st.text_area(
            "Areas to improve"
        )

        submitted = st.form_submit_button(
            "Submit lesson report",
            type="primary"
        )

        if submitted:

            try:

                supabase.table("lesson_reports").insert(
                    {
                        "student_name": student_name,
                        "tutor_name": tutor_name,
                        "subject": subject,
                        "lesson_date": str(lesson_date),
                        "topic": topic,
                        "lesson_summary": lesson_summary,
                        "homework": homework,
                        "areas_to_improve": areas_to_improve
                    }
                ).execute()

                st.success(
                    "Lesson report submitted successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not submit lesson report: {e}"
                )

    st.subheader("My submitted reports")

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "You have not submitted any lesson reports yet."
            )

    except Exception as e:

        st.error(
            f"Could not load your reports: {e}"
        )


# ============================================================
# TUTOR PORTAL
# ============================================================

def tutor_portal():

    tutor = tutor_profile()

    if not tutor:

        st.error(
            "Your tutor profile could not be found."
        )

        st.write(
            f"Logged in as: {current_email()}"
        )

        return

    page = tutor_sidebar()

    if page == "Dashboard":
        tutor_dashboard(tutor)

    elif page == "My Students":
        tutor_students(tutor)

    elif page == "My Timetable":
        tutor_timetable(tutor)

    elif page == "Attendance":
        tutor_attendance(tutor)

    elif page == "Lesson Reports":
        tutor_reports(tutor)

    footer()


# ============================================================
# APPLICATION ENTRY
# ============================================================

if "user" not in st.session_state:

    login()

else:

    role = get_role()

    if role == "admin":

        admin_portal()

    elif role == "tutor":

        tutor_portal()

    else:

        st.title("📚 Boomatt Academy")

        st.error(
            "This account has not been assigned a portal role."
        )

        st.write(
            f"Logged in as: {current_email()}"
        )

        if st.button("Log out"):
            logout()
