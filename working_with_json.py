import json
from pathlib import Path

# How to write data into json file

# moives = [
#     {"id": 1, "title": "All is well", "year": 2002},
#     {"id": 2, "title": "Big Brother", "year": 2010},
#     {"id": 3, "title": "Pushpa", "year": 2012},
#     {"id": 4, "title": "Avengers", "year": 2024}
# ]


# data = json.dumps(moives)

# Path("movies_data.json").write_text(data)

data = Path("movies_data.json").read_text()
movies = json.loads(data)

# read all data at once
# print(movies)

print(movies[3]["title"])  # print : Avengers
