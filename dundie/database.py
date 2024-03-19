import json
from datetime import datetime

from dundie.settings import DATABASE_PATH, EMAIL_FROM
from dundie.utils.email import check_valid_email, send_email
from dundie.utils.users import generate_simple_password

EMPTY_DB = {"people": {}, "balance": {}, "movements": {}, "users": {}}


def connect() -> dict:
    """Connects to the database, returns dict data"""
    try:
        with open(DATABASE_PATH, "r") as database_file:
            return json.loads(database_file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return EMPTY_DB


def commit(db):
    """Save db back to the database file"""
    if db.keys() != EMPTY_DB.keys():
        raise ValueError("The database schema is not valid.")

    with open(DATABASE_PATH, "w") as database_file:
        database_file.write(json.dumps(db, indent=4))


def add_person(db, pk, data):
    """Saves person data to the database
    Email is unique (resolve by dictionary hash table)
    - If exists update, else create
    - Set initial balance
    - Generate password
    """
    if not check_valid_email(pk):
        raise ValueError(f"{pk}: invalid email")

    table = db["people"]
    person = table.get(pk, {})
    created = not bool(person)
    person.update(data)
    table[pk] = person
    if created:
        set_initial_balance(db, pk, person)
        password = set_initial_password(db, pk)
        send_email(
            EMAIL_FROM, pk, "Welcome to Dundie", f"Your password is {password}"
        )
        # TODO: encrypt password
    return person, created


def set_initial_password(db, pk):
    """Set initial password for a person"""
    db["users"].setdefault(pk, {})
    db["users"][pk]["password"] = generate_simple_password(8)
    return db["users"][pk]["password"]


def set_initial_balance(db, pk, person):
    """Set initial balance for a person"""
    value = 100 if person["role"] == "Manager" else 500  # noqa


def add_movement(db, pk, value, actor="system"):
    """Add a movement to the database"""
    movements = db["movement"].setdefault(pk, [])
    movements.append(
        {
            "date": datetime.now().isoformat(),
            "actor": "system",
            "value": value,
        }
    )

    db["balance"][pk] = sum([item["value"] for item in movements])
