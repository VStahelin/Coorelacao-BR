from bs4 import BeautifulSoup
import requests
from googletrans import Translator
from collections.abc import Iterable


# TODO criar uma thread para essa funcao
def tradutor(texto):
    translator = Translator()
    return translator.translate(line, dest='pt').text


def ehInteravel(obj):
    return isinstance(obj, Iterable)


if __name__ == "__main__":
    url = "https://tylervigen.com/page?page=1"  # Url do site do Tyler TODO: automatizar essa parte
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    elementos_html = soup.find_all("table", attrs={"class": "container"})

    aux = 0
    print("----------")
    print("")
    for line in elementos_html:
        if ehInteravel(line.table):
            for table in line.table:
                if aux < 4:
                    print(table)
                    aux += 1
                else:
                    break
            print("")
            print("----------")
            print("")
            aux = 0
