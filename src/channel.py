import os
import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = Channel.get_service()
        self.id = channel_id
        self.channel_dict = self.url = self.title = self.description =\
            self.subscriberCount = self.videoCount = self.viewCount = None
        self.__get_channel_info()

    @property
    def channel_id(self):
        return self.id

    def __get_channel_info(self):
        self.channel_dict = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.url = "https://www.youtube.com/channel/" + self.channel_id
        self.title = self.channel_dict["items"][0]["snippet"]["title"]
        self.description = self.channel_dict["items"][0]["snippet"]["description"]
        self.subscriberCount = int(self.channel_dict["items"][0]["statistics"]["subscriberCount"])
        self.videoCount = int(self.channel_dict["items"][0]["statistics"]["videoCount"])
        self.viewCount = int(self.channel_dict["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other):
        return self.subscriberCount == other.subscriberCount

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # Обновляем информацию о канале, которая могла измениться с момента инициализации экземпляра класса.
        self.__get_channel_info()
        print(json.dumps(self.channel_dict, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        with open(filename, "w") as file_to_write:
            json.dump(self.channel_dict, file_to_write)

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

