import os
from pathlib import Path

abs_path = Path(__file__).parent.resolve()
cv_url = "https://drive.google.com/uc?export=download&id=17FfTBIJjN4vfJAICJ9NIeT6GUo590nYm"

data_path = os.path.join(abs_path, "data")
cv_path = os.path.join(data_path, "cv.pdf")
