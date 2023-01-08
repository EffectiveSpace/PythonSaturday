def read_file():
    with open('test1.txt', 'r') as file:
        data = file.read().split("\n")
        data.remove("")
    return data