from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def index():
    items = load_candidates_from_json()
    return render_template('list.html', items=items)


@app.route("/candidate/<int:pk>")
def candidate(pk):
    candidate = get_candidate(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/candidate/<name>")
def candidate_name(name):
    candidates = get_candidates_by_name(name)
    total = len(candidates)
    return render_template('search.html', candidates=candidates, total=total)


@app.route("/skill/<skill_name>")
def candidates_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    total = len(candidates)
    return render_template('skill.html', candidates=candidates, total=total, skill_name=skill_name)


if __name__ == '__main__':
    app.run(debug=True)
