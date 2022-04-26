import threading



class VideoStreaming:
    """
    video streaming Single Threading for every Videos frems
    """

    def __init__(self,
                 host,
                 port,
                 resolution=(640, 480),
                 framerate=30,
                 quality=50,
                 name=None,
                 ):
        """
        :param host: ip address of the streaming server
        :param port: port of the streaming server
        :param resolution: resolution of the video
        :param framerate: framerate of the video
        :param quality: quality of the video
        :param name: name of the video
        """
        self.host = host
        self.port = port
        self.resolution = resolution
        self.framerate = framerate
        self.quality = quality
        self.name = name
        self.stream = None
        self.stopped = False
        self.thread = None

    def start(self):
        """
        start the video streaming
        """
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()
        return self

    def run(self):
        """
        run the video streaming
        """
        raise NotImplementedError

    def update(self, frame):
        """
        update the video streaming
        :param frame: frame to update
        """
        raise NotImplementedError

    def stop(self):
        """
        stop the video streaming
        """
        self.stopped = True
        return self

    def join(self):
        """
        join the video streaming thread
        """
        self.thread.join()
        return self