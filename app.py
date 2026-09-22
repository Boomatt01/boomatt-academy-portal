import streamlit as st
from supabase_client import supabase
from datetime import date


# ============================================================
# BOOMATT ACADEMY — PROFESSIONAL PORTAL
# ============================================================

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #F5F7FA;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #0F2747;
        border-right: none;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #102A43 !important;
        font-weight: 700 !important;
    }

    p, label {
        color: #52606D;
    }


    /* ---------- SIDEBAR ---------- */

    .brand-box {
        padding: 10px 5px 25px 5px;
    }

    .brand-icon {
        font-size: 38px;
        margin-bottom: 8px;
    }

    .brand-name {
        font-size: 23px;
        font-weight: 800;
        color: white;
        letter-spacing: -0.5px;
    }

    .brand-tagline {
        font-size: 11px;
        color: #B8C7D9;
        line-height: 1.5;
        margin-top: 5px;
    }

    .portal-label {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.3px;
        color: #9FB3C8;
        margin-top: 12px;
        margin-bottom: 15px;
    }


    /* ---------- DASHBOARD HERO ---------- */

    .dashboard-hero {
        background: #102A43;
        border-radius: 18px;
        padding: 30px 32px;
        margin-bottom: 25px;
    }

    .dashboard-hero-title {
        color: white;
        font-size: 30px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .dashboard-hero-text {
        color: #D9E2EC;
        font-size: 14px;
    }


    /* ---------- METRICS ---------- */

    .metric-box {
        background: white;
        border: 1px solid #E4E7EB;
        border-radius: 15px;
        padding: 21px;
        min-height: 125px;
        box-shadow: 0 2px 8px rgba(16, 42, 67, 0.04);
    }

    .metric-title {
        font-size: 11px;
        font-weight: 700;
        color: #829AB1;
        letter-spacing: 0.8px;
    }

    .metric-number {
        font-size: 30px;
        font-weight: 800;
        color: #102A43;
        margin-top: 8px;
    }

    .metric-description {
        font-size: 12px;
        color: #7B8794;
        margin-top: 3px;
    }


    /* ---------- SECTION ---------- */

    .section-title {
        font-size: 19px;
        font-weight: 750;
        color: #102A43;
        margin-top: 28px;
        margin-bottom: 14px;
    }


    /* ---------- QUICK ACTION CARDS ---------- */

    .action-box {
        background: white;
        border: 1px solid #E4E7EB;
        border-radius: 15px;
        padding: 20px;
        min-height: 125px;
        box-shadow: 0 2px 8px rgba(16, 42, 67, 0.035);
    }

    .action-icon {
        font-size: 24px;
        margin-bottom: 10px;
    }

    .action-title {
        color: #102A43;
        font-size: 15px;
        font-weight: 700;
    }

    .action-text {
        color: #7B8794;
        font-size: 12px;
        margin-top: 5px;
    }


    /* ---------- LOGIN ---------- */

    .login-space {
        height: 80px;
    }

    .login-brand {
        text-align: center;
        font-size: 45px;
    }

    .login-title {
        text-align: center;
        color: #102A43;
        font-size: 31px;
        font-weight: 800;
    }

    .login-subtitle {
        text-align: center;
        color: #7B8794;
        font-size: 14px;
        margin-bottom: 25px;
    }


    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 9px;
        min-height: 42px;
        font-weight: 650;
    }


    /* ---------- FORMS ---------- */

    [data-testid="stForm"] {
        background: white;
        border: 1px solid #E4E7EB;
        border-radius: 15px;
        padding: 22px;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #9FB3C8;
        font-size: 11px;
        padding-top: 35px;
        padding-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
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
        <div class="footer">
            © 2026 Boomatt Academy · Building Confident Learners, One Lesson at a Time
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, number, description):
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">{title}</div>
            <div class="metric-number">{number}</div>
            <div class="metric-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AUTHENTICATION
# ============================================================

def login():

    st.markdown("<div class='login-space'></div>", unsafe_allow_html=True)

    left, middle, right = st.columns([1, 2, 1])

    with middle:

        st.markdown(
            "<div class='login-brand'>📚</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='login-title'>Boomatt Academy</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="login-subtitle">
                Building Confident Learners, One Lesson at a Time
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.form("login_form"):

            email = st.text_input(
                "Email address",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            submitted = st.form_submit_button(
                "Sign in",
                type="primary",
                use_container_width=True
            )

            if submitted:

                if not email or not password:

                    st.warning(
                        "Please enter your email address and password."
                    )

                else:

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
                            f"Login failed: {e}"
                        )

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

    # Current test tutor
    if email == "test@gmail.com":
        return "tutor"

    # Tutors registered in database
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

    except Exception:
        pass

    return "unknown"


# ============================================================
# SIDEBAR
# ============================================================

def admin_sidebar():

    st.sidebar.markdown(
        """
        <div class="brand-box">

            <div class="brand-icon">
                📚
            </div>

            <div class="brand-name">
                Boomatt Academy
            </div>

            <div class="brand-tagline">
                Building Confident Learners,<br>
                One Lesson at a Time
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='portal-label'>ACADEMY ADMINISTRATOR</div>",
        unsafe_allow_html=True
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

    if st.sidebar.button(
        "Log out",
        use_container_width=True
    ):
        logout()

    return page


def tutor_sidebar():

    st.sidebar.markdown(
        """
        <div class="brand-box">

            <div class="brand-icon">
                📚
            </div>

            <div class="brand-name">
                Boomatt Academy
            </div>

            <div class="brand-tagline">
                Building Confident Learners,<br>
                One Lesson at a Time
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='portal-label'>TUTOR PORTAL</div>",
        unsafe_allow_html=True
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

    st.markdown(
        """
        <div class="dashboard-hero">

            <div class="dashboard-hero-title">
                Welcome back, Academy Director 👋
            </div>

            <div class="dashboard-hero-text">
                Manage learners, tutors, lessons and academy
                operations from one place.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

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

        lessons = (
            supabase
            .table("timetable")
            .select("id")
            .execute()
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            metric_card(
                "STUDENTS",
                len(students.data or []),
                "Learners in the academy"
            )

        with c2:
            metric_card(
                "TUTORS",
                len(tutors.data or []),
                "Teaching team"
            )

        with c3:
            metric_card(
                "PARENTS",
                len(parents.data or []),
                "Parent records"
            )

        with c4:
            metric_card(
                "LESSONS",
                len(lessons.data or []),
                "Timetable entries"
            )

    except Exception as e:

        st.error(
            f"Could not load dashboard: {e}"
        )

    st.markdown(
        "<div class='section-title'>Academy workspace</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    actions = [
        (
            c1,
            "👨‍🎓",
            "Students",
            "Manage learner records."
        ),
        (
            c2,
            "👨‍🏫",
            "Tutors",
            "Manage your teaching team."
        ),
        (
            c3,
            "📅",
            "Timetable",
            "Organise lessons and schedules."
        ),
        (
            c4,
            "📖",
            "Reports",
            "Track teaching and learning."
        )
    ]

    for column, icon, title, description in actions:

        with column:

            st.markdown(
                f"""
                <div class="action-box">

                    <div class="action-icon">
                        {icon}
                    </div>

                    <div class="action-title">
                        {title}
                    </div>

                    <div class="action-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        "<div class='section-title'>Recent timetable</div>",
        unsafe_allow_html=True
    )

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
                "No timetable entries have been added yet."
            )

    except Exception as e:

        st.error(
            f"Could not load timetable: {e}"
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
            type="primary",
            use_container_width=True
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

    st.markdown("### Current students")

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
            type="primary",
            use_container_width=True
        )

        if submitted:

            if not full_name or not email:

                st.warning(
                    "Please enter the tutor's name and email."
                )

            else:

                try:

                    supabase.table("tutors").insert(
                        {
                            "full_name": full_name,
                            "email": email.lower().strip(),
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

    st.markdown("### Current tutors")

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
            type="primary",
            use_container_width=True
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

    st.markdown("### Current parents")

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
            "Add timetable entry",
            type="primary",
            use_container_width=True
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
                    "Timetable entry added successfully."
                )

            except Exception as e:

                st.error(
                    f"Could not add timetable entry: {e}"
                )

    st.markdown("### Current timetable")

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
                "No timetable entries yet."
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
        "Record and monitor lesson attendance."
    )

    with st.form("attendance_form"):

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
            type="primary",
            use_container_width=True
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

    st.markdown("### Attendance records")

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
        "Review teaching, learning progress and homework."
    )

    with st.form("lesson_report_form"):

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
            type="primary",
            use_container_width=True
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

    st.markdown("### Lesson reports")

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
            type="primary",
            use_container_width=True
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

    st.markdown("### Payment records")

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

    st.markdown(
        f"""
        <div class="dashboard-hero">

            <div class="dashboard-hero-title">
                Welcome, {tutor_name} 👋
            </div>

            <div class="dashboard-hero-text">
                Your Boomatt Academy teaching workspace.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

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
            metric_card(
                "MY STUDENTS",
                len(students),
                "Learners assigned to you"
            )

        with c2:
            metric_card(
                "MY LESSONS",
                len(timetable.data or []),
                "Scheduled lessons"
            )

        with c3:
            metric_card(
                "REPORTS",
                len(reports.data or []),
                "Reports submitted"
            )

    except Exception as e:

        st.error(
            f"Could not load tutor overview: {e}"
        )

    st.markdown(
        "<div class='section-title'>Your workspace</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    actions = [
        (
            c1,
            "👨‍🎓",
            "My Students",
            "View learners assigned to you."
        ),
        (
            c2,
            "📅",
            "My Timetable",
            "View your teaching schedule."
        ),
        (
            c3,
            "📝",
            "Lesson Reports",
            "Record learning and homework."
        )
    ]

    for column, icon, title, description in actions:

        with column:

            st.markdown(
                f"""
                <div class="action-box">

                    <div class="action-icon">
                        {icon}
                    </div>

                    <div class="action-title">
                        {title}
                    </div>

                    <div class="action-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


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
        "Learners currently assigned to your timetable."
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

            with st.container(border=True):

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
                            st.write(
                                f"**Year / Grade**\n\n"
                                f"{data.get('year_grade', '')}"
                            )

                        with c2:
                            st.write(
                                f"**School**\n\n"
                                f"{data.get('school', '')}"
                            )

                        with c3:
                            st.write(
                                f"**Subjects**\n\n"
                                f"{data.get('subjects', '')}"
                            )

                except Exception:
                    pass

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
            .order("created_at", desc=False)
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
            type="primary",
            use_container_width=True
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

    st.markdown("### My attendance records")

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "You have not recorded any attendance yet."
            )

    except Exception as e:

        st.error(
            f"Could not load attendance: {e}"
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
        "Record what was taught, learner progress and homework."
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
            type="primary",
            use_container_width=True
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

    st.markdown("### My lesson reports")

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
            f"Could not load lesson reports: {e}"
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

        st.title("Boomatt Academy")

        st.error(
            "This account has not been assigned a portal role."
        )

        st.write(
            f"Logged in as: {current_email()}"
        )

        if st.button("Log out"):

            logout()
