def count_points(compiled_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {"1": 0, "2": 0, "3": 0, "4": 0}

    for item in compiled_list:
        if item == "1":
            result["1"] += 1
        elif item == "2":
            result["2"] += 1
        elif item == "3":
            result["3"] += 1
        else:
            result["4"] += 1

    return result

def most_answered(dictionary: dict[str, int]) -> str:
    checker: int = 0
    most_chosen_choice: str = ""

    for item in dictionary:
        if dictionary[item] > checker:
            checker = dictionary[item]
            most_chosen_choice = item
    
    return most_chosen_choice


def find_villain(most_chosen_choice: str) -> str:
    if most_chosen_choice == '1':
        return 'Scar'
    elif most_chosen_choice == '2':
        return 'Maleficent'
    elif most_chosen_choice == '3':
        return 'Evil Queen'
    else:
        return 'Ursula'

def corresponding_link_getter(villain: str) -> str:
    if villain == 'Scar':
        return f"/static/Scar.jpg"
    elif villain == 'Maleficent':
        return f"/static/Maleficent.jpg"
    elif villain == 'Evil Queen':
        return f"/static/Evil_Queen.jpg"
    else:
        return f"/static/Ursula.jpg"

class user:
    id: int
    first_name: str
    last_name: str
    house: str

    def __init__(self, id: int, fname: str, lname: str, house: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.house = house