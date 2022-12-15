import json

# в файле содержатся данные о пользователях
FILE_NAME = 'candidates.json'


def load_candidates(FILE_NAME):
    """Функция загружаетданные из файла candidates.json"""
    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_candidates_from_json():
    """ Функция показывает всех кандидатов из файла candidates.json"""
    return load_candidates(FILE_NAME)


def get_candidate(pk):
    """ Функция взвращает кандидата по pk"""
    for candidate in load_candidates(FILE_NAME):
        if candidate['id'] == pk:
            return candidate
    return


def get_candidates_by_name(candidate_name):
    """ Функция взвращает кандидатов по совпадению. Выведит всех кандидатов, в имени у которых содержится candidate_name"""
    candidates_name = []
    for candidate in load_candidates(FILE_NAME):
        if candidate_name.lower() in candidate['name'].lower():
            candidates_name.append(candidate)
    return candidates_name


def get_candidates_by_skill(skill_name):
    """ Функция взвращает кандидатаов по навыку"""
    candidates_skills = []
    for candidate in load_candidates(FILE_NAME):
        skills = candidate['skills'].split(", ")
        for skill in skills:
            if skill_name.lower() == skill.lower():
                candidates_skills.append(candidate)
    return candidates_skills
