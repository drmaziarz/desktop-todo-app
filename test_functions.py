import os
from functions import get_todos, write_todos

FILEPATH = "test_todos.txt"
TEST_TODOS = ["Buy milk\n", "Do laundry\n", "Pay bills\n"]


def test_get_todos():
    with open(FILEPATH, "w") as file:
        file.writelines(TEST_TODOS)

    todos = get_todos(FILEPATH)
    assert todos == TEST_TODOS

    os.remove(FILEPATH)


def test_write_todos():
    write_todos(TEST_TODOS, FILEPATH)

    with open(FILEPATH, "r") as file:
        todos = file.readlines()
    assert todos == TEST_TODOS

    os.remove(FILEPATH)
