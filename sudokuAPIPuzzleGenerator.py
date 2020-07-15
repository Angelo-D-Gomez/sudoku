# API taken from http://www.cs.utep.edu/cheon/ws/sudoku/
import requests

response = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=2')
json_response = response.json()
json_squares = json_response['squares']
sudokuBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(8):
    for j in range(8):
        for item in json_squares:
            if item['x'] == j:
                if item['y'] == i:
                    sudokuBoard[i][j] = item['value']


