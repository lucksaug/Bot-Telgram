#Importação da biblioteca necessária para consumir a API
import requests as rq


#classe principal 
class Desculpa():
    #URL da API utilizada 
    url = 'https://excuser.herokuapp.com/v1/excuse/'

    #Método responsável por transformar a url da API em uma URL específica
    def acrescentar_na_URL(self, link, opcao):
        link += opcao
        return link
        
    #Método responsável por transformar a API consumida em uma lista
    def request_na_api(self, url):
        requisicao = rq.get(url)
        desculpa = requisicao.json()
        return desculpa

    #Método responsável por extrair somente o necessário da API
    def devolver_desculpa(self, url):
        lista = self.request_na_api(url)
        texto = lista[0]['excuse']
        return texto