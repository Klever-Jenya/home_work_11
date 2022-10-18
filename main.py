from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route("/")
def index():
    """Главная страничка"""
    candidates = utils.get_candidate_by_all()
    return render_template("list.html", candidates=candidates)

@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    if not candidate:
        return "Не найдено"
    return render_template("single.html", candidate=candidate)

@app.route("/skill/<skill>")
def get_candidates_by_skill(skill):
    candidates = utils.get_candidates_by_skill(skill)
    candidates_count = len(candidates)
    return render_template("skill.html",
                           candidates=candidates,
                           candidates_count=candidates_count,
                           skill=skill
                           )

@app.route("/search/<name>")
def get_candidates_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    candidates_count = len(candidates)
    return render_template("search.html",
                           candidates=candidates,
                           candidates_count=candidates_count
                           )



app.run(debug=True)
