import uuid
from rentomatic.domain import room


def test_room_model_from_dict():
    code = uuid.uuid4()
    room_object = room.Room.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.04,
            'latitude': 53.43
        }
    )

    assert room_object.code == code
    assert room_object.size == 200
    assert room_object.price == 10
    assert room_object.longitude == -0.04
    assert room_object.latitude == 53.43


def test_room_model_to_dict():
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }


    room_obj = room.Room.from_dict(room_dict)
    assert room_obj.to_dict() == room_dict


def test_room_model_comparison():
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }

    room1 = room.Room.from_dict(room_dict)
    room2 = room.Room.from_dict(room_dict)
    assert room1 == room2

