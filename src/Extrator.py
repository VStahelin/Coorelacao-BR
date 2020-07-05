from bs4 import BeautifulSoup
import requests
from src.models.LinhaDeRelacao import LinhaDeRelacao
from src.models.Coorelacao import Coorelacao
from googletrans import Translator
from collections.abc import Iterable


# TODO criar uma thread para essa funcao
def tradutor(texto):
    translator = Translator()
    return translator.translate(elemento, dest='pt').text


def ehInteravel(obj):
    return isinstance(obj, Iterable)


if __name__ == "__main__":
    url = "https://tylervigen.com/page?page=1"  # Url do site do Tyler TODO: automatizar essa parte
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    elementos_html = soup.find_all("table", attrs={"class": "container"})

    coorelacoes = []
    for elemento in elementos_html:
        item_aux = 0
        ja_teve_titulo = False
        coorelacao = Coorelacao()
        if ehInteravel(elemento.table):
            for linha in elemento.table:
                dados = LinhaDeRelacao()
                for font in linha.find_all("td"):
                    if font.text.strip():
                        if item_aux == 1:
                            coorelacao.appendNoCabecario(font.text)
                        elif item_aux == 2:
                            if ja_teve_titulo:
                                dados.adicionaValor(font.text)
                            else:
                                dados.setarTitulo(font.text)
                                ja_teve_titulo = True
                        elif item_aux == 3:
                            if ja_teve_titulo:
                                dados.adicionaValor(font.text)
                            else:
                                dados.setarTitulo(font.text)
                                ja_teve_titulo = True

                        # print("{}: {}".format(aux, font.text))
                    else:
                        if item_aux == 2:
                            coorelacao.setaItem1(dados)
                            item_aux += 1
                        elif item_aux == 3:
                            coorelacao.setaItem2(dados)
                        else:
                            item_aux += 1
                        dados = LinhaDeRelacao()
                        ja_teve_titulo = False
            aux = 0
        coorelacoes.append(coorelacao)
    for relacao in coorelacoes:
        print(str(relacao))