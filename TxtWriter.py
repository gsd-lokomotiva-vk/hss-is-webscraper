from typing import List


def export_data_to_txt_file(filepath: str, filename: str, data: str | List):
    with open(filepath + filename + ".txt", 'w', encoding="utf-8") as file:
        if isinstance(data, list):
            for element in data:
                file.write(element + "\n")
        if isinstance(data, str):
            file.write(data)
            
