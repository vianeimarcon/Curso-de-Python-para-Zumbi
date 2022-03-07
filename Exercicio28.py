import requests
from tkinter import *
from tkinter import ttk

def pegar_cotacoes():
    requisicao = requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CAD-BRL"
    )

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_cad = requisicao_dic['CADBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: U$ {cotacao_dolar}
    Dólar Canadense: $ {cotacao_cad}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    print(texto)


#pegar_cotacoes()

form = Tk()
form.title("Buscar Cotação Atual de Moedas ")
form.geometry("400x400")

texto = Label(form, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(form, text="Buscar Cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(form, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

form.mainloop()
