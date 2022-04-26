from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from decouple import config
import logging
import logging.handlers


LOG_FILENAME = 'videoStreammingByNetGear.log'

logging.basicConfig(filename=LOG_FILENAME, filemode='a',
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# Creating an object
my_logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=20000000, backupCount=5)

my_logger.addHandler(handler)


def main():
    options = {
        "multiclient_mode": False,
        "jpeg_compression": True,
        "jpeg_compression_quality": 90,
        "jpeg_compression_fastdct": True,
        "jpeg_compression_fastupsample": True
    }
    # stream = VideoGear(source=config("RTSP_URL", cast=int)).start()
    # stream = VideoGear(source="water.mp4").start()
    # stream = VideoGear(source=0).start()
    # stream = VideoGear(source="/home/rafiq/AlterSense/Helios_G/rtsp_streaming/forbidden_activity_rtsp_streaming/water.mp4").start()
    stream = VideoGear(source="/home/rafiq/AlterSense/Helios_G/rtsp_streaming/forbidden_activity_rtsp_streaming/7th_March.mp4").start()
    # stream = VideoGear(source="rtsp://admin:Admin2020@202.74.243.147:554/trackID=4").start()
    server = NetGear(
        # address=config('CLIENT_ADDRESS', cast=str),
        # port=config('PORT', cast=int),
        address='192.168.1.151',
        port=5003,
        protocol="tcp",
        pattern=2,
        logging=True,
        **options
    )
    while True:
        try:
            my_logger.info("Streaming...")
            frame = stream.read()
            if frame is None:
                break
            server.send(frame)
            # _, buffer = cv2.imencode('.jpg', frame)
            # frame = buffer.tobytes()
        except Exception as e:
            my_logger.debug(str(e))
            continue


if __name__ == "__main__":
    main()
