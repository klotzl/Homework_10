from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates: list[dict] = get_all()
    result: str = format_candidates(candidates)

    return result


@app.route("/candidate/<int:pk>")
def candidate_information(pk):
    candidate_list = []
    candidate = get_by_pk(pk)
    candidate_list.append(candidate)
    result = f'<img src={candidate["picture"]}>'
    result += format_candidates(candidate_list)

    return result


@app.route("/skills/<skill_name>")
def skill_page(skill_name):
    candidates = get_by_skill(skill_name)
    result = format_candidates(candidates)

    return result


app.run()
