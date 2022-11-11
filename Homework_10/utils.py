import json


def load_candidates() -> list[dict]:
    '''Функция, которая загрузит данные из файла в формате json'''
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_all() -> list[dict]:
    '''Функция, которая покажет всех кандидатов'''
    return load_candidates()


def get_by_pk(pk):
    '''Функция, которая вернет кандидата по pk'''
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return "Not found"


def get_by_skill(skill_name):
    '''Функция, которая вернет кандидатов по навыку'''
    result = []
    candidates = load_candidates()
    for candidate in candidates:
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            result.append(candidate)
    return result


def format_candidates(candidates: list[dict]) -> str:
    '''Функция, которая форматирует список кандидатов'''
    result = '<pre>'

    for candidate in candidates:
        result += f""" 
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
                    """
    result += '</pre>'
    return result
