from models import User, Phone

def phone_saver(name: str, phones: str) -> bool:
    """Gets `name` and `phones` and saves them as related objects in DB 

    Args:
        name (str): Contact name
        phones (str): Contact's phones, separated by `\\n` 

    Returns:
        bool: Operation success status
    """
    if name and phones:
        user = User.add(name)
        for phone in phones.split("\n"):
            Phone.add(phone, user)
        return True
    return False

def show_all_phones() -> list:
    """Gets all contacts from DB and returns a list of tuples
    for displaying contacts in search list

    Returns:
        list: [list of tuple([name: str, phones: str, user_id: int])]
    """
    return [tuple([user.name, ", ".join([phone.phone for phone in user.phones]), user.id]) for user in User.all()]

def show_all_for_name(name: str) -> list:
    """Filters contacts by 'name' from DB and returns a list of tuples
    for displaying contacts in search list

    Returns:
        list: [list of tuple([name: str, phones: str, user_id: int])]
    """
    print(name)
    return [tuple([user.name, " ".join([phone.phone for phone in user.phones]), user.id]) for user in User.find_by_name(name)]

def show_all_for_phone(phone: str) -> list:
    """Filters contacts by 'phone' from DB and returns a list of tuples
    for displaying contacts in search list

    Returns:
        list: [list of tuple([name: str, phones: str, user_id: int])]
    """
    res = [tuple([user.name, " ".join([phone.phone for phone in user.phones]), user.id]) for user in User.find_by_phone(phone)]
    return res