# import os
# from pathlib import Path
#
# import requests
#
# abs_path = Path(__file__).parent.resolve()
# cv_url = "https://drive.google.com/uc?export=download&id=17FfTBIJjN4vfJAICJ9NIeT6GUo590nYm"
#
# data_path = os.path.join(abs_path, "data")
# cv_path = os.path.join(data_path, "cv.pdf")
#
#
# def get_or_download_cv():
#     Path(data_path).mkdir(parents=True, exist_ok=True)
#     if not os.path.isfile(cv_path):
#         response = requests.get(cv_url, allow_redirects=True)
#         open(cv_path, "wb").write(response.content)
#
#     return cv_path
#
#
# print(get_or_download_cv())

# import csv
# import os
#
#
# repos_csv = os.path.join(abs_path, "data/repositories.csv")
# with open(repos_csv, 'r') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     for row in reader:
#         print(row)
