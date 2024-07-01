FACE_CARDS = {1: "A", 11: "J", 12: "Q", 13: "K"}


def value_to_face(value: int):
    return FACE_CARDS.get(value, value)
