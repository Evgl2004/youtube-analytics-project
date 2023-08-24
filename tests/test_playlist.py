import pytest
import datetime
from src.playlist import PlayList


@pytest.fixture()
def coll_test_playlist():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_properties(coll_test_playlist):
    assert coll_test_playlist.title == "Moscow Python Meetup №81"
    assert coll_test_playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(coll_test_playlist):
    duration = coll_test_playlist.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


def test_show_best_video(coll_test_playlist):
    assert coll_test_playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
