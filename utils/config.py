import sys, os


EXECUTABLE_TESSERACT_FILE = "D:\\Softwares\\Tesseract\\tesseract.exe"


def get_list_pokemon():
    path = "./pokemon.txt"
    if not os.path.exists(path):
        path = "../pokemon.txt"
    file = open(path, "r")
    print("Get list Pokemon from pokemon.txt...")
    list_pokemon = []
    while True:
        line = file.readline()
        if not line:
            break
        list_pokemon.append(line.strip().lower())

    file.close()
    print("Done, ", list_pokemon)
    return list_pokemon


def resource(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Then use this function to find the asset, eg: resource("my_file")
