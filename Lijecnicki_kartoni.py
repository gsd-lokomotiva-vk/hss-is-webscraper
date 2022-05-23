from bs4 import BeautifulSoup
import JSONManager
import BrowserOperations
import TxtWriter
import ExcelWriter
import HTMLInspector

config = JSONManager.load_json("Lijecnicki kartoni.json")

excel_workbook_name = config["filename"]
excel_workbook_path = config["path"]
txt_file_name = config["filename"]
txt_file_path = config["path"]


def download_page_data():
    return BrowserOperations.get_page_content(config["webpage"])


def save_page_data_as_txt(page_data, filename: str = None, filepath: str = None):
    if filename is None:
        if filepath is None:
            TxtWriter.export_data_to_txt_file(txt_file_path, txt_file_name, page_data)
        else:
            TxtWriter.export_data_to_txt_file(filepath, txt_file_name, page_data)
    else:
        if filename is None:
            TxtWriter.export_data_to_txt_file(filepath, txt_file_name, page_data)
        else:
            TxtWriter.export_data_to_txt_file(filepath, filename, page_data)


def prepare_excel_workbook():
    ExcelWriter.create_new_workbook(excel_workbook_name, excel_workbook_path)


def get_tables(page_data):
    tables = page_data.find_all('table', attrs={'class': 'siroko'})
    return tables


def prepare_excel_data(page_data, table_index: int = 0):
    """returns table headers, table rows"""
    page_data = BeautifulSoup(page_data, "html.parser")
    tables = get_tables(page_data)
    headers = HTMLInspector.get_table_headers(tables[table_index])
    rows = HTMLInspector.get_table_rows(tables[table_index])
    return headers, rows


def run():
    page_data = download_page_data()

    save_page_data_as_txt(page_data)

    prepare_excel_workbook()

    waiting_approval = [["Neodobreni zahtjevi"]]
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, waiting_approval)
    headers, rows = prepare_excel_data(page_data, 0)
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, headers)
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, rows)

    approved = [["Odobreni zahtjevi"]]
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, approved)
    headers, rows = prepare_excel_data(page_data, 1)
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, headers)
    ExcelWriter.append_rows_to_existing_workbook(excel_workbook_name, excel_workbook_path, rows)
    
