import pytest
from src.video import Video, PLVideo


@pytest.fixture()
def coll_test_video():
    return Video('AWX4JnAnjBE')


@pytest.fixture()
def coll_test_pl_video():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_str_video(coll_test_video):
    assert str(coll_test_video) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_str_pl_video(coll_test_pl_video):
    assert str(coll_test_pl_video) == 'MoscowPython Meetup 78 - вступление'


def test_pl_video(coll_test_pl_video):
    assert coll_test_pl_video.pl_video_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'