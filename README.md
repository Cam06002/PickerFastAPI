# PickerFastAPI
Package built for data pipeline using FastAPI and SQLAlchemy with NFLPicker data from previously uploaded repository.

Using my existing NFLPicker script, I scraped pro-football-reference.com, pulling only the data for the Green Bay Packers and the San Francisco 49ers. I then populated CSV files with the data I pulled for each team.

Using SQLAlchemy and FastAPI, I built models and a connection between my CSV files and a Postgres database. I used a modular technique to allow me to customize the process as I go, and for added reusability. The last piece of the puzzle was a load file that brought everything together and pushed everything from my CSV to my Postgres database. Then, I used the Git functions in PyCharm to push the files to this repository.
