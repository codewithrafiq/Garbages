from flask import Flask
from pathlib import Path
from konfik import Konfik

# Define the config path
BASE_DIR = Path(__file__).parent
# Initialize the konfik class
konfik = Konfik(config_path=BASE_DIR / "config.toml")
# Get the config dict from the konfik class
config = konfik.config


app = Flask(__name__, template_folder="templates")


from project import routes
