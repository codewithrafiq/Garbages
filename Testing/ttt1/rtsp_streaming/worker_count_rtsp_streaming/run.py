from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from decouple import config
import logging
import logging.handlers
from konfik import Konfik
from pathlib import Path

BASE_DIR = Path(__file__).parent
konfik = Konfik(config_path= BASE_DIR / "config.toml").config


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
    # stream = VideoGear(source="vid.mp4").start()
    # stream = VideoGear(source=config("RTSP_URL",cast=str)).start()
    # stream = VideoGear(source="rtsp://admin:Admin2020@202.74.243.147:554/trackID=5").start()
    # stream = VideoGear(source=konfik.rtsp.url).start()
    stream = VideoGear(source="/home/rafiq/AlterSense/Helios_G/rtsp_streaming/worker_count_rtsp_streaming/b2b-Video-03132022_153734.mp4").start()
    server = NetGear(
        address=konfik.netgear.ip,
        port= konfik.netgear.port,
        protocol="tcp",
        pattern=2,
        logging=True,
        **options
    )
    while True:
        try:
            my_logger.info("Streaming...")
            frame = stream.read()
            # frame = frame / 255.0
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
