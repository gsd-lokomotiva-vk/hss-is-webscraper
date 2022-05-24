from bs4 import BeautifulSoup
import JSONManager
import BrowserOperations
import TxtWriter
import ExcelWriter
import HTMLInspector
from typing import List


config = JSONManager.load_json("Pregled_clanstva.json")
main_webpage = config["webpage"]

excel_workbook_name = config["filename"]
excel_workbook_path = config["path"]
txt_file_name = config["filename"]
txt_file_path = config["path"]


def extract_members_webpages(webpage_data):
    return HTMLInspector.get_links_in_div(webpage_data, {"class": "twelve columns", "style": "text-align: center"})


def download_member_details(webpage: str):
    return BrowserOperations.get_page_content(webpage)


def download_members_webpage():
    return BrowserOperations.get_page_content(main_webpage)


def get_ime(webpage_data) -> str:
    try:
        ime = webpage_data.find("input", attrs={"id": "MainContent_txtIme"})["value"]
    except KeyError:
        return ""
    return ime


def get_prezime(webpage_data) -> str:
    try:
        prezime = webpage_data.find("input", attrs={"id": "MainContent_txtPrezime"})["value"]
    except KeyError:
        return ""
    return prezime


def get_spol(webpage_data) -> str:
    try:
        spol = webpage_data.find("option", attrs={"selected": "selected"})["value"]
    except KeyError:
        return ""
    if spol:
        return "Muško"
    return "Žensko"


def get_OIB(webpage_data) -> str:
    try:
        OIB = webpage_data.find("input", attrs={"id": "MainContent_txtOIB"})["value"]
    except KeyError:
        return ""
    return OIB


def get_datum_rodjenja(webpage_data) -> str:
    try:
        datum_rodjenja = webpage_data.find("input", attrs={"id": "MainContent_DatumRodjenja"})["value"]
    except KeyError:
        return ""
    return datum_rodjenja


def get_mjesto_rodjenja(webpage_data) -> str:
    try:
        mjesto_rodjenja = webpage_data.find("input", attrs={"id": "MainContent_txtMjestoRodjenja"})["value"]
    except KeyError:
        return ""
    return mjesto_rodjenja


def get_adresa(webpage_data) -> str:
    try:
        adresa = webpage_data.find("input", attrs={"id": "MainContent_txtAdresaStanovanja"})["value"]
    except KeyError:
        return ""
    return adresa


def get_mjesto_stanovanja(webpage_data) -> str:
    try:
        mjesto_stanovanja = webpage_data.find("input", attrs={"id": "MainContent_hfMjestoLabela"})["value"]
    except KeyError:
        return ""
    return mjesto_stanovanja


def get_HSS(webpage_data) -> str:
    try:
        HSS = webpage_data.find("input", attrs={"id": "MainContent_txtHSSiskaznica"})["value"]
    except KeyError:
        return ""
    return HSS


def get_OI(webpage_data) -> str:
    try:
        OI = webpage_data.find("input", attrs={"id": "MainContent_txtbrojOI"})["value"]
    except KeyError:
        return ""
    return OI


def get_OI_trajna(webpage_data) -> str:
    try:
        OI_trajna = webpage_data.find("input", attrs={"id": "MainContent_trajnaOsobnaVrijednost"})["value"]
    except KeyError:
        return ""
    if OI_trajna:
        return "DA"
    return "NE"


def get_OI_datum(webpage_data) -> str:
    try:
        OI_datum = webpage_data.find("input", attrs={"id": "MainContent_txtDatumVazenjaOsobneIskaznice"}["value"])
    except KeyError:
        return ""
    return OI_datum


def get_OI_mjesto(webpage_data) -> str:
    try:
        OI_mjesto = webpage_data.find("input", attrs={"id": "MainContent_txtOsobnaIzdanaU"})["value"]
    except KeyError:
        return ""
    return OI_mjesto


def get_putovnica(webpage_data) -> str:
    try:
        putovnica = webpage_data.find("input", attrs={"id": "MainContent_txtBrojPutovnice"})["value"]
    except KeyError:
        return ""
    return putovnica


def get_putovnica_datum(webpage_data) -> str:
    try:
        putovnica_datum = webpage_data.find("input", attrs={"id": "MainContent_txtPutovnicaVrijediDo"})["value"]
    except KeyError:
        return ""
    return putovnica_datum


def get_putovnica_mjesto(webpage_data) -> str:
    try:
        putovnica_mjesto = webpage_data.find("input", attrs={"id": "MainContent_txtPutovnicaIzdanaU"})["value"]
    except KeyError:
        return ""
    return putovnica_mjesto


def get_drzavljanstvo(webpage_data) -> str:
    try:
        drzavljanstvo = webpage_data.find("input", attrs={"id": "MainContent_txtDrzavljanstvo"})["value"]
    except KeyError:
        return ""
    return drzavljanstvo


def get_strucna_sprema(webpage_data) -> str:
    try:
        strucna_sprema = webpage_data.find("input", attrs={"id": "MainContent_txtStrucnaSprema"})["value"]
    except KeyError:
        return ""
    return strucna_sprema


def get_zaposlenje(webpage_data) -> str:
    try:
        zaposlenje = webpage_data.find("input", attrs={"id": "MainContent_txtZaposlenje"})["value"]
    except KeyError:
        return ""
    return zaposlenje


def get_hobi(webpage_data) -> str:
    try:
        hobi = webpage_data.find("input", attrs={"id": "MainContent_txtHobi"})["value"]
    except KeyError:
        return ""
    return hobi


def get_ziro_racun(webpage_data) -> str:
    try:
        ziro_racun = webpage_data.find("input", attrs={"id": "MainContent_txtBankaNaziv"})["value"]
    except KeyError:
        return ""
    return ziro_racun


def get_telefon_kucni(webpage_data) -> str:
    try:
        telefon_kucni = webpage_data.find("input", attrs={"id": "MainContent_txtTelefonKucni"})["value"]
    except KeyError:
        return ""
    return telefon_kucni


def get_telefon_posao(webpage_data) -> str:
    try:
        telefon_posao = webpage_data.find("input", attrs={"id": "MainContent_txtTelefonPosao"})["value"]
    except KeyError:
        return ""
    return telefon_posao


def get_mobitel1(webpage_data) -> str:
    try:
        mobitel1 = webpage_data.find("input", attrs={"id": "MainContent_txtMobitel1"})["value"]
    except KeyError:
        return ""
    return mobitel1


def get_mobitel2(webpage_data) -> str:
    try:
        mobitel2 = webpage_data.find("input", attrs={"id": "MainContent_txtMobitel2"})["value"]
    except KeyError:
        return ""
    return mobitel2


def get_email(webpage_data) -> str:
    try:
        email = webpage_data.find("input", attrs={"id": "MainContent_txtEmail"})["value"]
    except KeyError:
        return ""
    return email


def get_excel_data(webpage_data) -> List[List]:
    excel_data = [
        ["Ime:", get_ime(webpage_data)],
        ["Prezime:", get_prezime(webpage_data)],
        ["Spol:", get_spol(webpage_data)],
        ["OIB:", get_OIB(webpage_data)],
        ["Datum rođenja:", get_datum_rodjenja(webpage_data)],
        ["Mjesto rođenja:", get_mjesto_rodjenja(webpage_data)],
        ["Adresa stanovanja:", get_adresa(webpage_data)],
        ["Mjesto stanovanja:", get_mjesto_stanovanja(webpage_data)],
        ["HSS iskaznica:", get_HSS(webpage_data)],
        ["Broij OI:", get_OI(webpage_data)],
        ["Osobna trajna:", get_OI_trajna(webpage_data)],
        ["Osobna vrijedi do:", get_OI_datum(webpage_data)],
        ["Mjesto izdavanja osobne:", get_OI_mjesto(webpage_data)],
        ["Broj putovnica:", get_putovnica(webpage_data)],
        ["Putovnica vrijedi do:", get_putovnica_datum(webpage_data)],
        ["Mjesto izdavanja putovnice:", get_putovnica_mjesto(webpage_data)],
        ["Državljanstvo:", get_drzavljanstvo(webpage_data)],
        ["Stručna sprema:", get_strucna_sprema(webpage_data)],
        ["Zaposlenje:", get_zaposlenje(webpage_data)],
        ["Hobi:", get_hobi(webpage_data)],
        ["Žiro račun:", get_ziro_racun(webpage_data)],
        ["Telefon kućni:", get_telefon_kucni(webpage_data)],
        ["Telefon posao:", get_telefon_posao(webpage_data)],
        ["Mobitel 1:", get_mobitel1(webpage_data)],
        ["Mobitel 2:", get_mobitel2(webpage_data)],
        ["E-mail:", get_email(webpage_data)]
    ]

    return excel_data


def run():
    main_webpage_data = download_members_webpage()
    TxtWriter.export_data_to_txt_file(txt_file_path, txt_file_name, main_webpage_data)

    members_pages = extract_members_webpages(main_webpage_data)

    TxtWriter.export_data_to_txt_file(txt_file_path, txt_file_name + "_pages", members_pages)

    ExcelWriter.create_new_workbook(excel_workbook_path, excel_workbook_name)
    for i, member_page in enumerate(members_pages):
        member_details = download_member_details("https://hss-is.com" + str(member_page))
        member_details_soup = BeautifulSoup(member_details, "html.parser")
        TxtWriter.export_data_to_txt_file(
            txt_file_path, txt_file_name + get_ime(member_details_soup) + get_prezime(member_details_soup),
            member_details
        )
        ExcelWriter.export_to_excel_workbook(
            get_ime(member_details_soup) + get_prezime(member_details_soup),
            get_excel_data(member_details_soup),
            excel_workbook_path,
            excel_workbook_name,
        )
        
