from bs4 import BeautifulSoup
import requests

cookies = {
    'cookiesession1': '678A3F6F38D355DE2AE8C13502FF6294',
    '_ga': 'GA1.1.1843432756.1743798198',
    '_ga_HRW645ZPYT': 'GS1.1.1743801485.2.1.1743801486.59.0.0',
}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'cookiesession1=678A3F6F38D355DE2AE8C13502FF6294; _ga=GA1.1.1843432756.1743798198; _ga_HRW645ZPYT=GS1.1.1743801485.2.1.1743801486.59.0.0',
    'Referer': 'https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Opera GX";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.indec.gob.ar/Institucional/Indec/BasesDeDatos', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

urls = []
for a in soup.find_all("a"):
    href =  a.get("href")
    if href and "ftp/cuadros/menusuperior/eph" in href and "_txt.zip" in href:
        url_absoluta = "https://www.indec.gob.ar" + a["href"]
        anio = url_absoluta.split("_")[-2]
        trimestre = url_absoluta.split("_")[-4]
        if trimestre == "usu":
            trimestre = [x for x in url_absoluta.split("_")[-3] if x.isdigit()][0]

        urls.append({"url": url_absoluta, "año": anio, "trimestre": trimestre})
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


for url_info in urls:
    download_url(url_info["url"], f"data_zip/data_{url_info["trimestre"]}_{url_info["año"]}.zip")