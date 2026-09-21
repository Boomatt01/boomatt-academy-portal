import streamlit as st
from supabase_client import supabase

# ============================================================
# BOOMATT ACADEMY
# MASTER BRANDED PORTAL
# ============================================================

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# BOOMATT ACADEMY DESIGN SYSTEM
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

:root {
    --navy: #10233F;
    --blue: #2563EB;
    --blue-light: #EFF6FF;
    --green: #16A34A;
    --gold: #F59E0B;
    --background: #F7F9FC;
    --white: #FFFFFF;
    --text: #172033;
    --muted: #667085;
    --border: #E5EAF1;
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background: var(--background);
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    font-family: "Manrope", sans-serif !important;
    color: var(--navy) !important;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: var(--navy);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.boomatt-brand {
    padding: 8px 4px 22px 4px;
}

.boomatt-logo {
    width: 50px;
    height: 50px;
    background: white;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
    margin-bottom: 12px;
}

.boomatt-name {
    color: white;
    font-family: "Manrope", sans-serif;
    font-size: 24px;
    font-weight: 800;
}

.boomatt-tagline {
    color: rgba(255,255,255,0.70);
    font-size: 12px;
    line-height: 1.5;
    margin-top: 5px;
}

/* HERO */

.hero {
    background: linear-gradient(
        135deg,
        #10233F 0%,
        #1D4ED8 100%
    );

    border-radius: 22px;
    padding: 32px;
    margin-bottom: 25px;

    box-shadow:
        0 15px 35px rgba(16,35,63,0.13);
}

.hero h1 {
    color: white !important;
    font-size: 34px;
    margin: 0 0 8px 0;
}

.hero p {
    color: rgba(255,255,255,0.85);
    margin: 0;
    font-size: 15px;
}

/* METRIC CARDS */

.metric-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 21px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(16,35,63,0.045);
}

.metric-label {
    color: var(--muted);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .04em;
}

.metric-value {
    color: var(--navy);
    font-family: "Manrope", sans-serif;
    font-size: 31px;
    font-weight: 800;
    margin-top: 7px;
}

.metric-note {
    color: var(--muted);
    font-size: 12px;
    margin-top: 4px;
}

/* QUICK CARDS */

.quick-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 19px;
    min-height: 110px;
    box-shadow: 0 5px 18px rgba(16,35,63,0.04);
}

.quick-icon {
    font-size: 24px;
    margin-bottom: 8px;
}

.quick-title {
    color: var(--navy);
    font-weight: 800;
    font-size: 14px;
}

.quick-text {
    color: var(--muted);
    font-size: 12px;
    margin-top: 4px;
}

/* FORMS */

[data-testid="stForm"] {
    background: white;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 23px;
    box-shadow: 0 5px 18px rgba(16,35,63,0.03);
}

/* BUTTONS */

div.stButton > button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
}

/* LOGIN */

.login-container {
    max-width: 500px;
    margin: 7vh auto 0 auto;
}

.login-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 38px;
    box-shadow: 0 20px 55px rgba(16,35,63,0.10);
    text-align: center;
}

.login-icon {
    width: 68px;
    height: 68px;
    background: var(--navy);
    border-radius: 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    margin-bottom: 15px;
}

.login-title {
    color: var(--navy);
    font-family: "Manrope", sans-serif;
    font-size: 29px;
    font-weight: 800;
}

.login-subtitle {
    color: var(--muted);
    font-size: 14px;
    margin: 6px 0 25px 0;
}

/* FOOTER */

.footer {
    text-align: center;
    color: var(--muted);
    font-size: 12px;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

def sidebar_brand(role):

    st.sidebar.markdown(
        f"""
        <div class="boomatt-brand">

            <div class="boomatt-logo">
                📚
            </div>

            <div class="boomatt-name">
                Boomatt Academy
            </div>

            <div class="boomatt-tagline">
                Building Confident Learners,<br>
                One Lesson at a Time
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.caption(role)

    st.sidebar.divider()


def footer():

    st.markdown(
        """
        <div class="footer">
            © 2026 Boomatt Academy
            · Building Confident Learners, One Lesson at a Time
        </div>
        """,
        unsafe_allow_html=True
    )


def metric(label, value, note):

    return f"""
    <div class="metric-card">

        <div class="metric-label">
            {label}
        </div>

        <div class="metric-value">
            {value}
        </div>

        <div class="metric-note">
            {note}
        </div>

    </div>
    """


# ============================================================
# AUTHENTICATION
# ============================================================

def login():

    st.markdown(
        '<div class="login-container"><div class="login-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="login-icon">
            📚
        </div>

        <div class="login-title">
            Boomatt Academy
        </div>

        <div class="login-subtitle">
            Building Confident Learners, One Lesson at a Time
        </div>
        """,
        unsafe_allow_html=True
    )

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
                "Please enter your email and password."
            )

        else:

            try:

                response = (
                    supabase
                    .auth
                    .sign_in_with_password({
                        "email": email.strip().lower(),
                        "password": password
                    })
                )

                if response.user:

                    st.session_state.user = response.user

                    st.rerun()

            except Exception as e:

                st.error(
                    f"Login failed: {e}"
                )

    st.markdown(
        "</div></div>",
        unsafe_allow_html=True
    )

    footer()


def logout():

    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.clear()

    st.rerun()


def current_email():

    if "user" not in st.session_state:
        return None

    return st.session_state.user.email


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

    # Other tutors
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
# ADMIN NAVIGATION
# ============================================================

def admin_navigation():

    sidebar_brand(
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
        <div class="hero">

            <h1>
                Welcome back, Academy Director 👋
            </h1>

            <p>
                Manage learners, tutors, lessons and
                academy operations from one place.
            </p>

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

        c1.markdown(
            metric(
                "STUDENTS",
                len(students.data or []),
                "Learners in the academy"
            ),
            unsafe_allow_html=True
        )

        c2.markdown(
            metric(
                "TUTORS",
                len(tutors.data or []),
                "Teaching team"
            ),
            unsafe_allow_html=True
        )

        c3.markdown(
            metric(
                "PARENTS",
                len(parents.data or []),
                "Parent records"
            ),
            unsafe_allow_html=True
        )

        c4.markdown(
            metric(
                "LESSONS",
                len(lessons.data or []),
                "Timetable entries"
            ),
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error(
            f"Could not load dashboard: {e}"
        )

    st.markdown("### Academy workspace")

    a, b, c, d = st.columns(4)

    cards = [

        (
            a,
            "👨‍🎓",
            "Students",
            "Manage learner records."
        ),

        (
            b,
            "👨‍🏫",
            "Tutors",
            "Manage your teaching team."
        ),

        (
            c,
            "📅",
            "Timetable",
            "Organise lessons and schedules."
        ),

        (
            d,
            "📖",
            "Reports",
            "Track teaching and learning."
        )

    ]

    for column, icon, title, description in cards:

        with column:

            st.markdown(
                f"""
                <div class="quick-card">

                    <div class="quick-icon">
                        {icon}
                    </div>

                    <div class="quick-title">
                        {title}
                    </div>

                    <div class="quick-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Recent timetable")

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .order("created_at", desc=True)
            .limit(8)
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
# ADMIN — STUDENTS
# ============================================================

def admin_students():

    st.title("👨‍🎓 Students")

    st.caption(
        "Create and review learner profiles."
    )

    with st.form("student_form"):

        full_name = st.text_input(
            "Student Name"
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
            "Add Student",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "Student"
                ).insert({
                    "full_name": full_name,
                    "year_grade": year_grade,
                    "school": school,
                    "subjects": subjects
                }).execute()

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
            .order(
                "created_at",
                desc=True
            )
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
# ADMIN — TUTORS
# ============================================================

def admin_tutors():

    st.title("👨‍🏫 Tutors")

    st.caption(
        "Manage the Boomatt Academy teaching team."
    )

    with st.form("tutor_form"):

        full_name = st.text_input(
            "Tutor Name"
        )

        email = st.text_input(
            "Tutor Email"
        )

        subjects = st.text_input(
            "Subjects"
        )

        qualification = st.text_input(
            "Qualification"
        )

        submitted = st.form_submit_button(
            "Add Tutor",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "tutors"
                ).insert({
                    "full_name": full_name,
                    "email": email.lower().strip(),
                    "subjects": subjects,
                    "qualification": qualification
                }).execute()

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
            .order(
                "created_at",
                desc=True
            )
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
# ADMIN — PARENTS
# ============================================================

def admin_parents():

    st.title("👨‍👩‍👧 Parents")

    st.caption(
        "Manage parent and guardian records."
    )

    with st.form("parent_form"):

        full_name = st.text_input(
            "Parent Name"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone"
        )

        submitted = st.form_submit_button(
            "Add Parent",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "parents"
                ).insert({
                    "full_name": full_name,
                    "email": email,
                    "phone": phone
                }).execute()

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
            .order(
                "created_at",
                desc=True
            )
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
# ADMIN — TIMETABLE
# ============================================================

def admin_timetable():

    st.title("📅 Timetable")

    st.caption(
        "Create and review lesson schedules."
    )

    with st.form("timetable_form"):

        student_name = st.text_input(
            "Student Name"
        )

        tutor_name = st.text_input(
            "Tutor Name"
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

        start_time = st.text_input(
            "Start Time"
        )

        end_time = st.text_input(
            "End Time"
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
            "Add Timetable Entry",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "timetable"
                ).insert({
                    "student_name": student_name,
                    "tutor_name": tutor_name,
                    "subject": subject,
                    "day": day,
                    "start_time": start_time,
                    "end_time": end_time,
                    "status": status
                }).execute()

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
            .order(
                "created_at",
                desc=True
            )
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
# ADMIN — ATTENDANCE
# ============================================================

def admin_attendance():

    st.title("📝 Attendance")

    st.caption(
        "Record and review lesson attendance."
    )

    with st.form("attendance_form"):

        student_name = st.text_input(
            "Student Name"
        )

        tutor_name = st.text_input(
            "Tutor Name"
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
            "Save Attendance",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "attendance"
                ).insert({
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

    st.markdown("### Attendance records")

    try:

        result = (
            supabase
            .table("attendance")
            .select("*")
            .order(
                "lesson_date",
                desc=True
            )
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
# ADMIN — LESSON REPORTS
# ============================================================

def admin_reports():

    st.title("📖 Lesson Reports")

    st.caption(
        "Review and manage teaching reports."
    )

    with st.form("lesson_report_form"):

        student_name = st.text_input(
            "Student Name"
        )

        tutor_name = st.text_input(
            "Tutor Name"
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
            "Save Lesson Report",
            use_container_width=True
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

    st.markdown("### Lesson reports")

    try:

        result = (
            supabase
            .table("lesson_reports")
            .select("*")
            .order(
                "lesson_date",
                desc=True
            )
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
# ADMIN — PAYMENTS
# ============================================================

def admin_payments():

    st.title("💳 Payments")

    st.caption(
        "Track academy payment records."
    )

    with st.form("payment_form"):

        parent_name = st.text_input(
            "Parent Name"
        )

        student_name = st.text_input(
            "Student Name"
        )

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

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Save Payment",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "payments"
                ).insert({
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

    st.markdown("### Payment records")

    try:

        result = (
            supabase
            .table("payments")
            .select("*")
            .order(
                "payment_date",
                desc=True
            )
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

    page = admin_navigation()

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
# TUTOR
# ============================================================

def tutor_navigation():

    sidebar_brand(
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

    if st.sidebar.button(
        "Log out",
        use_container_width=True
    ):

        logout()

    return page


def tutor_profile():

    email = current_email()

    if not email:
        return None

    try:

        result = (
            supabase
            .table("tutors")
            .select("*")
            .eq(
                "email",
                email.lower().strip()
            )
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


def tutor_dashboard(tutor):

    tutor_name = tutor.get(
        "full_name",
        "Tutor"
    )

    st.markdown(
        f"""
        <div class="hero">

            <h1>
                Welcome, {tutor_name} 👋
            </h1>

            <p>
                Your Boomatt Academy teaching workspace
                is ready for today's lessons.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    try:

        timetable = (
            supabase
            .table("timetable")
            .select("student_name")
            .eq(
                "tutor_name",
                tutor_name
            )
            .execute()
        )

        students = {
            x.get("student_name")
            for x in (
                timetable.data or []
            )
            if x.get("student_name")
        }

        reports = (
            supabase
            .table("lesson_reports")
            .select("id")
            .eq(
                "tutor_name",
                tutor_name
            )
            .execute()
        )

        c1, c2, c3 = st.columns(3)

        c1.markdown(
            metric(
                "MY STUDENTS",
                len(students),
                "Learners assigned to you"
            ),
            unsafe_allow_html=True
        )

        c2.markdown(
            metric(
                "MY LESSONS",
                len(timetable.data or []),
                "Scheduled lessons"
            ),
            unsafe_allow_html=True
        )

        c3.markdown(
            metric(
                "LESSON REPORTS",
                len(reports.data or []),
                "Reports submitted"
            ),
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error(
            f"Could not load tutor overview: {e}"
        )

    st.markdown("### Your workspace")

    a, b, c = st.columns(3)

    cards = [

        (
            a,
            "👨‍🎓",
            "My Students",
            "View learners assigned to you."
        ),

        (
            b,
            "📅",
            "My Timetable",
            "View your teaching schedule."
        ),

        (
            c,
            "📝",
            "Lesson Reports",
            "Record learning and homework."
        )

    ]

    for column, icon, title, description in cards:

        with column:

            st.markdown(
                f"""
                <div class="quick-card">

                    <div class="quick-icon">
                        {icon}
                    </div>

                    <div class="quick-title">
                        {title}
                    </div>

                    <div class="quick-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


def tutor_students(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("👨‍🎓 My Students")

    st.caption(
        "Learners currently assigned to your timetable."
    )

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .eq(
                "tutor_name",
                tutor_name
            )
            .execute()
        )

        students = sorted({
            x.get("student_name")
            for x in (
                result.data or []
            )
            if x.get("student_name")
        })

        if not students:

            st.info(
                "No students have been assigned to you yet."
            )

            return

        for student in students:

            with st.container(border=True):

                st.markdown(
                    f"### 👤 {student}"
                )

                try:

                    info = (
                        supabase
                        .table("Student")
                        .select("*")
                        .eq(
                            "full_name",
                            student
                        )
                        .limit(1)
                        .execute()
                    )

                    if info.data:

                        data = info.data[0]

                        c1, c2, c3 = st.columns(3)

                        c1.write(
                            f"**Year / Grade**\n\n"
                            f"{data.get('year_grade', '')}"
                        )

                        c2.write(
                            f"**School**\n\n"
                            f"{data.get('school', '')}"
                        )

                        c3.write(
                            f"**Subjects**\n\n"
                            f"{data.get('subjects', '')}"
                        )

                except Exception:
                    pass

    except Exception as e:

        st.error(
            f"Could not load your students: {e}"
        )


def tutor_timetable(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("📅 My Timetable")

    st.caption(
        "Your assigned teaching schedule."
    )

    try:

        result = (
            supabase
            .table("timetable")
            .select("*")
            .eq(
                "tutor_name",
                tutor_name
            )
            .order(
                "created_at",
                desc=False
            )
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


def tutor_attendance(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("📝 Attendance")

    st.caption(
        "Record attendance for your lessons."
    )

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
            "Save Attendance",
            use_container_width=True
        )

        if submitted:

            try:

                supabase.table(
                    "attendance"
                ).insert({
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

    st.markdown("### My attendance records")

    try:

        result = (
            supabase
            .table("attendance")
            .select("*")
            .eq(
                "tutor_name",
                tutor_name
            )
            .order(
                "lesson_date",
                desc=True
            )
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


def tutor_reports(tutor):

    tutor_name = tutor.get(
        "full_name",
        ""
    )

    st.title("📖 Lesson Reports")

    st.caption(
        "Record what was taught, learner progress and homework."
    )

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
            "Submit Lesson Report",
            use_container_width=True
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
            .eq(
                "tutor_name",
                tutor_name
            )
            .order(
                "lesson_date",
                desc=True
            )
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

    page = tutor_navigation()

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
# MAIN APPLICATION
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
