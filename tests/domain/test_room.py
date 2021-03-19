import uuid
from rentomatic.domain import room


def test_room_mood_init():
    code = uuid.uuid4()
    room_object = room.Room(code, size=200, price=10,
                     longitude=-0.04, latitude=52.45)
    assert room_object.code == code
    assert room_object.size == 200
    assert room_object.price == 10
    assert room_object.longitude == -0.04
    assert room_object.latitude == 52.45
