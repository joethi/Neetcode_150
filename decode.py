# import requests
import pandas as pd

def decode_message(url):
    # Fetch the data from the URL
    df = pd.read_html(url)
    df = df[0]
    # Take the 0th row as the header
    df.columns = df.iloc[0]
    df = df[1:]  # Drop the original header row
    # Reset the index for cleaner presentation
    df.reset_index(drop=True, inplace=True)
    df["Character"] = df["Character"].apply(lambda x: x.encode('latin1').decode('utf-8'))
    df["x-coordinate"] = df["x-coordinate"].astype(int)
    df["y-coordinate"] = df["y-coordinate"].astype(int)
    # Parse the coordinates and characters
    positions = []
    tuples_list = list(zip(df["x-coordinate"], df["y-coordinate"], df["Character"]))
    positions = positions + tuples_list
    # Find the dimensions of the grid
    max_x = int(max(pos[0] for pos in positions))
    max_y = int(max(pos[1] for pos in positions))
    # print("positions:",positions)
    # Initialize the grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Populate the grid with characters
    for x, y, char in positions:
        grid[y][x] = char
    # Print the grid in the desired coordinate system
    print("Grid representation of 'F':")
    for y in range(max_y, -1, -1):  # Reverse the rows to match y increasing upwards
        for x in range(max_x + 1):
            print(grid[y][x], end='')
        print()  # Newline after each row

# URL_TO_THE_GOOGLE_DOC = "https://w3schools.com/python/demopage.htm"
# URL_TO_THE_GOOGLE_DOC = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
URL_TO_THE_GOOGLE_DOC = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
# Example usage
decode_message(URL_TO_THE_GOOGLE_DOC)



