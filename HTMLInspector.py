from bs4 import BeautifulSoup


def get_table_headers(table):
    table_header = table.find('thead')
    table_headers = table_header.find_all('th')
    headers = []
    
    for header in table_headers:
        headers.append(header.text.strip())
    return headers


def get_table_rows(table):
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    rows = []

    for table_row in table_rows:
        cols = table_row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        rows.append([ele for ele in cols if ele])
    return rows


def get_links_in_div(page_data, div_attrs):
    page_data = BeautifulSoup(page_data, "html.parser")
    data = page_data.find_all('div', attrs=div_attrs)
    links_in_div = []
    for div in data:
        links = div.find_all('a')
        for a in links:
            links_in_div.append(a['href'])
    return links_in_div
