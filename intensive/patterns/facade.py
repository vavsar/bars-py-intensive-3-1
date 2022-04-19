class WebSiteConverter:

    def __init__(self, audioconverter, videoconverter):
        self._audioconverter = audioconverter
        self._videoconverter = videoconverter

    def operation(self):
        results = []
        results.append("WebSiteConverter starts convertations:")
        results.append(self._audioconverter.convert_audio())
        results.append(self._videoconverter.convert_video())

        return "\n".join(results)


class BaseConverter:

    def _get_stream_method(self):
        pass

    def _check_stream_data(self):
        pass


class AudioConverter(BaseConverter):

    def convert_audio(self):
        self._get_stream_method()
        self._check_stream_data()

        return "Audio convertation done"


class VideoConverter(BaseConverter):

    def convert_video(self):
        self._get_stream_method()
        self._check_stream_data()

        return "Video convertation done"


def client_code(facade):

    print(facade.operation())


if __name__ == "__main__":
    audio_converter = AudioConverter()
    video_converter = VideoConverter()
    facade = WebSiteConverter(audio_converter, video_converter)
    client_code(facade)
