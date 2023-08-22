import os
from googleapiclient.discovery import build


class Video:
    """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""

    def __init__(self, video_id):
        self.youtube = self.__class__.get_service()
        self.id = video_id
        self.channel_dict = self.url = self.title = self.description = self.likeCount = self.viewCount = None
        self.__get_video_info()

    @property
    def video_id(self):
        return self.id

    def __get_video_info(self):
        self.video_dict = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.url = "https://www.youtube.com/video/" + self.video_id
        self.title = self.video_dict["items"][0]["snippet"]["title"]
        self.description = self.video_dict["items"][0]["snippet"]["description"]
        self.likeCount = int(self.video_dict["items"][0]["statistics"]["likeCount"])
        self.viewCount = int(self.video_dict["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return self.title

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))


class PLVideo(Video):
    def __init__(self, video_id, pl_video_id):
        super().__init__(video_id)
        self._pl_video_id = pl_video_id

    @property
    def pl_video_id(self):
        return self._pl_video_id
