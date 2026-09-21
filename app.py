from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# ---------------------------------------------------------
# BOOMATT ACADEMY - SIMPLE SUPERPROF-STYLE PROTOTYPE
# ---------------------------------------------------------

tutors = [
    {
        "id": 1,
        "name": "Tutor Olatunji",
        "subject": "English",
        "speciality": "English Language, IELTS, GCSE, SATs",
        "location": "Lagos, Nigeria",
        "price": 5000,
        "rating": 5.0,
        "lessons": 2000,
        "image": "https://images.unsplash.com/photo-1544717305-2782549b5136"
    },
    {
        "id": 2,
        "name": "Tutor Esther",
        "subject": "Mathematics",
        "speciality": "Primary Mathematics, KS2, KS3, GCSE",
        "location": "Lagos, Nigeria",
        "price": 4500,
        "rating": 4.9,
        "lessons": 850,
        "image": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce"
    },
    {
        "id": 3,
        "name": "Tutor Precious",
        "subject": "Science",
        "speciality": "Biology, Chemistry, Physics",
        "location": "Nigeria",
        "price": 5000,
        "rating": 4.8,
        "lessons": 600,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2"
    }
]


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Boomatt Academy | Find Your Perfect Tutor</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f7f9fc;
            color: #172033;
        }

        nav {
            background: white;
            padding: 20px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #eee;
        }

        .logo {
            font-size: 25px;
            font-weight: 800;
            color: #123c7a;
        }

        .logo span {
            color: #f59e0b;
        }

        nav a {
            text-decoration: none;
            color: #333;
            margin-left: 25px;
            font-weight: 500;
        }

        .hero {
            background: linear-gradient(
                120deg,
                #0d3268,
                #1557a6
            );

            color: white;
            padding: 90px 7%;
            text-align: center;
        }

        .hero h1 {
            font-size: 48px;
            max-width: 850px;
            margin: auto;
            line-height: 1.15;
        }

        .hero p {
            font-size: 19px;
            margin: 20px auto 35px;
            max-width: 650px;
            opacity: .9;
        }

        .search-box {
            background: white;
            padding: 10px;
            max-width: 850px;
            margin: auto;
            border-radius: 10px;
            display: flex;
            gap: 10px;
        }

        .search-box input,
        .search-box select {
            flex: 1;
            padding: 16px;
            border: none;
            outline: none;
            font-size: 15px;
            background: #f4f6f9;
            border-radius: 6px;
        }

        .search-btn {
            background: #f59e0b;
            color: white;
            border: none;
            padding: 0 30px;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }

        .section {
            padding: 70px 7%;
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
        }

        .section-title h2 {
            font-size: 34px;
        }

        .section-title p {
            color: #666;
            margin-top: 10px;
        }

        .subjects {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
        }

        .subject {
            background: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,.05);
        }

        .subject-icon {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .tutors {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }

        .tutor-card {
            background: white;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,.07);
        }

        .tutor-card img {
            width: 100%;
            height: 230px;
            object-fit: cover;
        }

        .tutor-info {
            padding: 22px;
        }

        .tutor-info h3 {
            margin-bottom: 7px;
        }

        .subject-name {
            color: #1557a6;
            font-weight: bold;
        }

        .rating {
            color: #f59e0b;
            margin: 10px 0;
        }

        .price {
            font-size: 20px;
            font-weight: bold;
            margin: 15px 0;
        }

        .view-btn {
            display: block;
            text-align: center;
            background: #123c7a;
            color: white;
            padding: 13px;
            text-decoration: none;
            border-radius: 6px;
        }

        .how {
            background: #eef4fb;
        }

        .steps {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
        }

        .step {
            text-align: center;
        }

        .number {
            width: 55px;
            height: 55px;
            margin: auto auto 15px;
            border-radius: 50%;
            background: #123c7a;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 20px;
        }

        .cta {
            padding: 80px 7%;
            text-align: center;
            background: #123c7a;
            color: white;
        }

        .cta h2 {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .cta button {
            margin-top: 25px;
            padding: 15px 30px;
            border: none;
            background: #f59e0b;
            color: white;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }

        footer {
            background: #091c38;
            color: white;
            padding: 35px 7%;
            text-align: center;
        }

        @media(max-width: 700px) {

            .hero h1 {
                font-size: 35px;
            }

            .search-box {
                flex-direction: column;
            }

            .search-btn {
                padding: 15px;
            }

            nav {
                flex-direction: column;
                gap: 15px;
            }
        }

    </style>
</head>


<body>

<nav>

    <div class="logo">
        Boomatt<span>Academy</span>
    </div>

    <div>
        <a href="/">Find a Tutor</a>
        <a href="#subjects">Subjects</a>
        <a href="#how">How It Works</a>
        <a href="#tutor">Become a Tutor</a>
    </div>

</nav>


<section class="hero">

    <h1>
        Find the Right Tutor for Your Learning Journey
    </h1>

    <p>
        Connect with qualified tutors and learn online
        from the comfort of your home.
    </p>


    <form class="search-box" action="/search">

        <input
            type="text"
            name="subject"
            placeholder="What do you want to learn?"
        >

        <select name="level">

            <option value="">Select level</option>

            <option>Primary</option>
            <option>Secondary</option>
            <option>GCSE</option>
            <option>A-Level</option>
            <option>IELTS</option>
            <option>Adult Learner</option>

        </select>

        <button class="search-btn">
            Find Tutor
        </button>

    </form>

</section>


<section class="section" id="subjects">

    <div class="section-title">

        <h2>Explore Subjects</h2>

        <p>
            Find experienced tutors across different
            subjects and learning levels.
        </p>

    </div>


    <div class="subjects">

        <div class="subject">
            <div class="subject-icon">📚</div>
            <h3>English</h3>
            <p>Grammar, Writing, Reading & IELTS</p>
        </div>

        <div class="subject">
            <div class="subject-icon">🔢</div>
            <h3>Mathematics</h3>
            <p>Primary, KS3, GCSE & more</p>
        </div>

        <div class="subject">
            <div class="subject-icon">🔬</div>
            <h3>Science</h3>
            <p>Biology, Chemistry & Physics</p>
        </div>

        <div class="subject">
            <div class="subject-icon">📖</div>
            <h3>Literature</h3>
            <p>Analysis, essays and examinations</p>
        </div>

        <div class="subject">
            <div class="subject-icon">🗣️</div>
            <h3>Communication</h3>
            <p>Speaking and communication skills</p>
        </div>

    </div>

</section>


<section class="section">

    <div class="section-title">

        <h2>Meet Our Tutors</h2>

        <p>
            Learn from experienced and dedicated educators.
        </p>

    </div>


    <div class="tutors">

        {% for tutor in tutors %}

        <div class="tutor-card">

            <img src="{{ tutor.image }}">

            <div class="tutor-info">

                <h3>{{ tutor.name }}</h3>

                <div class="subject-name">
                    {{ tutor.subject }}
                </div>

                <p>
                    {{ tutor.speciality }}
                </p>

                <div class="rating">
                    ★ {{ tutor.rating }}
                    · {{ tutor.lessons }}+ lessons
                </div>

                <div>
                    📍 {{ tutor.location }}
                </div>

                <div class="price">
                    ₦{{ "{:,}".format(tutor.price) }}/hour
                </div>

                <a
                    class="view-btn"
                    href="/tutor/{{ tutor.id }}"
                >
                    View Profile
                </a>

            </div>

        </div>

        {% endfor %}

    </div>

</section>


<section class="section how" id="how">

    <div class="section-title">

        <h2>How Boomatt Academy Works</h2>

        <p>
            Getting started is simple.
        </p>

    </div>


    <div class="steps">

        <div class="step">

            <div class="number">1</div>

            <h3>Find a Tutor</h3>

            <p>
                Search for a tutor based on subject,
                level and learning needs.
            </p>

        </div>


        <div class="step">

            <div class="number">2</div>

            <h3>View Their Profile</h3>

            <p>
                Explore qualifications, experience,
                teaching style and availability.
            </p>

        </div>


        <div class="step">

            <div class="number">3</div>

            <h3>Book a Trial</h3>

            <p>
                Arrange an introductory lesson with
                your selected tutor.
            </p>

        </div>


        <div class="step">

            <div class="number">4</div>

            <h3>Start Learning</h3>

            <p>
                Continue with regular lessons and
                track your learning progress.
            </p>

        </div>

    </div>

</section>


<section class="cta" id="tutor">

    <h2>Are You a Tutor?</h2>

    <p>
        Join Boomatt Academy and connect with learners
        looking for quality education.
    </p>

    <button>
        Apply to Become a Tutor
    </button>

</section>


<footer>

    <strong>Boomatt Academy</strong>

    <p>
        Building Confident Learners, One Lesson at a Time.
    </p>

    <p>
        © 2026 Boomatt Academy. All Rights Reserved.
    </p>

</footer>

</body>
</html>
"""


# ---------------------------------------------------------
# TUTOR PROFILE
# ---------------------------------------------------------

PROFILE_PAGE = """
<!DOCTYPE html>

<html>

<head>

<title>{{ tutor.name }} | Boomatt Academy</title>

<style>

body {
    font-family: Arial;
    background: #f5f7fa;
    margin: 0;
}

.container {
    max-width: 1000px;
    margin: 60px auto;
    padding: 20px;
}

.profile {
    background: white;
    padding: 35px;
    border-radius: 15px;
    display: flex;
    gap: 35px;
}

.profile img {
    width: 260px;
    height: 260px;
    object-fit: cover;
    border-radius: 12px;
}

h1 {
    color: #123c7a;
}

.subject {
    color: #1557a6;
    font-weight: bold;
}

.rating {
    color: #f59e0b;
    margin: 15px 0;
}

.price {
    font-size: 25px;
    font-weight: bold;
    margin: 20px 0;
}

button {
    background: #f59e0b;
    border: none;
    color: white;
    padding: 15px 25px;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
}

@media(max-width:700px) {

    .profile {
        flex-direction: column;
    }

    .profile img {
        width: 100%;
    }

}

</style>

</head>


<body>

<div class="container">

    <div class="profile">

        <img src="{{ tutor.image }}">

        <div>

            <h1>{{ tutor.name }}</h1>

            <div class="subject">
                {{ tutor.subject }}
            </div>

            <div class="rating">
                ★ {{ tutor.rating }}
                · {{ tutor.lessons }}+ lessons
            </div>

            <p>
                {{ tutor.speciality }}
            </p>

            <p>
                📍 {{ tutor.location }}
            </p>

            <div class="price">
                ₦{{ "{:,}".format(tutor.price) }}/hour
            </div>

            <button onclick="alert('Trial booking system coming next!')">
                Book a Trial Class
            </button>

        </div>

    </div>

</div>

</body>

</html>
"""


# ---------------------------------------------------------
# SEARCH
# ---------------------------------------------------------

SEARCH_PAGE = """
<!DOCTYPE html>

<html>

<head>

<title>Find a Tutor | Boomatt Academy</title>

<style>

body {
    font-family: Arial;
    background: #f5f7fa;
}

.container {
    max-width: 1100px;
    margin: 50px auto;
    padding: 20px;
}

.card {
    background: white;
    padding: 25px;
    margin: 20px 0;
    border-radius: 10px;
}

a {
    background: #123c7a;
    color: white;
    padding: 10px 18px;
    text-decoration: none;
    border-radius: 5px;
}

</style>

</head>

<body>

<div class="container">

<h1>Find a Tutor</h1>

<p>
Search results for:
<strong>{{ subject or "All Subjects" }}</strong>
</p>


{% for tutor in results %}

<div class="card">

<h2>{{ tutor.name }}</h2>

<p>
<strong>{{ tutor.subject }}</strong>
</p>

<p>
{{ tutor.speciality }}
</p>

<p>
⭐ {{ tutor.rating }}
</p>

<p>
₦{{ "{:,}".format(tutor.price) }}/hour
</p>

<a href="/tutor/{{ tutor.id }}">
View Tutor
</a>

</div>

{% else %}

<p>No tutors found.</p>

{% endfor %}

</div>

</body>

</html>
"""


# ---------------------------------------------------------
# ROUTES
# ---------------------------------------------------------

@app.route("/")
def home():

    return render_template_string(
        HOME_PAGE,
        tutors=tutors
    )


@app.route("/search")
def search():

    subject = request.args.get("subject", "").lower()

    if subject:

        results = [
            tutor for tutor in tutors
            if subject in tutor["subject"].lower()
            or subject in tutor["speciality"].lower()
        ]

    else:

        results = tutors

    return render_template_string(
        SEARCH_PAGE,
        results=results,
        subject=subject
    )


@app.route("/tutor/<int:tutor_id>")
def tutor_profile(tutor_id):

    tutor = next(
        (t for t in tutors if t["id"] == tutor_id),
        None
    )

    if not tutor:
        return "Tutor not found", 404

    return render_template_string(
        PROFILE_PAGE,
        tutor=tutor
    )


# ---------------------------------------------------------
# START APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
