import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

abs_path = Path(__file__).parent.resolve()
cv_id = os.getenv("GOOGLE_DRIVE_FILE_ID")
cv_url = f"https://drive.google.com/uc?export=download&id={cv_id}"

data_path = os.path.join(abs_path, "data")
cv_path = os.path.join(data_path, "cv.pdf")
