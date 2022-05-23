from bs4 import BeautifulSoup
import JSONManager
import BrowserOperations
import TxtWriter
import ExcelWriter
import HTMLInspector


config = JSONManager.load_json("Pregled natjecanja.json")

excel_workbook_name = config["filename"]
excel_workbook_path = config["path"]
txt_file_name = config["filename"]
txt_file_path = config["path"]


def download_all_pages(no_of_pages: int = 100):
    page = 1
    prepare_excel_workbook()
    while True:
        if page > no_of_pages:
            break
        data = download_page_data(config["webpage"] + config["nextPage"] + str(page))
        save_page_data_as_txt(data, txt_file_name + str(page), txt_file_path)
        headers, rows = prepare_excel_data(data)
        if page == 1:
            ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, headers)
        ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, rows)
        
        try:
            temp = rows[0]
        except IndexError:
            break

        page += 1


def get_tables(page_data):
    tables = page_data.find_all('table', attrs={'style': 'width: 100%;'})
    return tables


def prepare_excel_data(page_data):
    """returns (table headers, table rows)"""
    page_data = BeautifulSoup(page_data, "html.parser")
    tables = get_tables(page_data)
    headers = HTMLInspector.get_table_headers(tables[0])
    rows = HTMLInspector.get_table_rows(tables[0])
    return headers, rows


def download_page_data(webpage: str):
    return BrowserOperations.get_page_content(webpage)


def prepare_excel_workbook():
    ExcelWriter.create_new_workbook(excel_workbook_name, excel_workbook_path)


def save_page_data_as_txt(page_data, filename: str = None, filepath: str = None):
    if filename is None:
        TxtWriter.export_data_to_txt_file(txt_file_path, txt_file_name, page_data)
    else:
        TxtWriter.export_data_to_txt_file(filepath, filename, page_data)


def run(no_of_pages: int = 100):
    download_all_pages(no_of_pages)
    
