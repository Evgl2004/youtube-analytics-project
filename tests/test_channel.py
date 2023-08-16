import pytest
import json
from src.channel import Channel


@pytest.fixture()
def coll_test_chanel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture()
def coll_test_chanel_highload():
    return Channel('UCwHL6WHUarjGfUM_586me8w')


def test_class_init(coll_test_chanel):
    assert coll_test_chanel.title == "MoscowPython"
    assert coll_test_chanel.url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"


def test_change_channel_id(coll_test_chanel):
    with pytest.raises(AttributeError):
        coll_test_chanel.channel_id = "Новое название"


def test_get_service():
    assert str(type(Channel.get_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_to_json(coll_test_chanel):
    coll_test_chanel.to_json("test_to_json.json")
    with open("test_to_json.json") as json_file:
        json.loads(json_file.read()) == coll_test_chanel.channel_dict


def test_str(coll_test_chanel):
    assert coll_test_chanel.__str__() == "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"


def test_add(coll_test_chanel, coll_test_chanel_highload):
    assert coll_test_chanel + coll_test_chanel_highload == 102400


def test_sub(coll_test_chanel, coll_test_chanel_highload):
    assert coll_test_chanel - coll_test_chanel_highload == -49800
    assert coll_test_chanel_highload - coll_test_chanel == 49800


def test_gt(coll_test_chanel, coll_test_chanel_highload):
    assert (coll_test_chanel > coll_test_chanel_highload) == False


def test_ge(coll_test_chanel, coll_test_chanel_highload):
    assert (coll_test_chanel >= coll_test_chanel_highload) == False


def test_lt(coll_test_chanel, coll_test_chanel_highload):
    assert (coll_test_chanel < coll_test_chanel_highload) == True


def test_le(coll_test_chanel, coll_test_chanel_highload):
    assert (coll_test_chanel <= coll_test_chanel_highload) == True


def test_eq(coll_test_chanel, coll_test_chanel_highload):
    assert (coll_test_chanel == coll_test_chanel_highload) == False

