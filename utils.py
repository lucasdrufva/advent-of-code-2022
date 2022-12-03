import requests

def get_data(day: int):
    try:
        with open(f"input{day}.txt") as file:
            return file.read().strip()
    except FileNotFoundError:
        with open("session.txt") as file:
            session = file.read().strip()
        
        response = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies={"session": session}) 

        with open(f"input{day}.txt", "w") as file:
            file.write(response.text[:-1])

        return response.text[:-1]

