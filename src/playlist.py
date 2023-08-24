from os import getenv
from googleapiclient.discovery import build
from datetime import timedelta
from isodate import parse_duration


class PlayList:
    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""
        self.youtube = self.__class__.get_service()
        self.id = playlist_id
        self.playlist_dict = self.url = self.title = None
        self.__get_playlist_info()

    @property
    def playlist_id(self):
        return self.id

    @property
    def total_duration(self):
        return self.__get_duration()

    def __get_playlist_info(self):
        self.playlist_dict = self.youtube.playlists().list(id=self.playlist_id, part='snippet', maxResults=50).execute()
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        self.title = self.playlist_dict["items"][0]["snippet"]["title"]

    def __str__(self):
        return f'{self.title} ({self.url})'

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=getenv('YT_API_KEY'))

    def __get_playlist_videos(self):
        return self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails', maxResults=50).execute()

    def __get_video_ids(self):
        return [video['contentDetails']['videoId'] for video in self.__get_playlist_videos()['items']]

    def __get_video_response(self):
        video_ids = self.__get_video_ids()
        return self.youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()

    def __get_duration(self):
        video_response = self.__get_video_response()
        duration = timedelta(seconds=0)
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            duration = duration + parse_duration(video['contentDetails']['duration'])

        return duration

    def show_best_video(self):
        dict_for_sort = {}
        video_response = self.__get_video_response()
        for video in video_response['items']:
            dict_for_sort[video["id"]] = int(video["statistics"]["likeCount"])

        dict_for_sort = sorted(dict_for_sort.items(), key=lambda i: i[1], reverse=True)

        return "https://youtu.be/" + dict_for_sort[0][0]