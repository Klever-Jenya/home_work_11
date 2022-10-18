import json

def load_candidates(): # возвращает список всех кандидатов
    with open ("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)  #список словарей

def get_candidate_by_all():
    return load_candidates()

def get_candidate_by_pk(pk): # возвращает одного кандидата по его id
    for candidate in load_candidates():
        if pk == candidate["id"]:
            return candidate
    return None

def get_candidates_by_skill(skill): # возвращает кандидатов по навыку
    candidates = []
    for candidate in load_candidates():
        skills = candidate["skills"].lower().split(", ")
        if skill in skills:
            candidates.append(candidate)
    return candidates

def get_candidates_by_name(name): # возвращает кандидатов по имени
    candidates = []
    for candidate in load_candidates():
        if name in candidate["name"]:
            candidates.append(candidate)
    return candidates
