import PySimpleGUI as sg
import requests

sg.theme('PythonPlus')
layout = [[sg.Text('Insira a moeda de origem:', size=(30,1)), sg.Combo(['Real (BRL)','Dólar (USD)','Euro (EUR)', 'Bitcoin (BTC)'], key='-Moeda1', size=(15,1))],
          [sg.Text('Insira a moeda de destino:', size=(30,1)), sg.Combo(['Real (BRL)','Dólar (USD)','Euro (EUR)'], key='-Moeda2', size=(15,1))],
          [sg.Submit('Converter'), sg.Cancel('Cancelar')]
]

window = sg.Window("Conversor de Moeda Versão 1.0", layout)

event, values = window.read()
window.close()

moeda1 = values['-Moeda1']
if moeda1 == 'Dólar (USD)':
    moeda1 = 'Dólar'
    abreviar1 = 'USD'
if moeda1 == 'Bitcoin (BTC)':
    moeda1 = 'Bitcoin'
    abreviar1 = 'BTC'
if moeda1 == 'Euro (EUR)':
    moeda1 = 'Euro'
    abreviar1 = 'EUR'
if moeda1 == 'Real (BRL)':
    moeda1 = 'Real'
    abreviar1 = 'BRL'

moeda2 = values['-Moeda2']
if moeda2 == 'Dólar (USD)':
    moeda2 = 'Dólar'
    abreviar2 = 'USD'
if moeda2 == 'Euro (EUR)':
    moeda2 = 'Euro'
    abreviar2 = 'EUR'
if moeda2 == 'Real (BRL)':
    moeda2 = 'Real'
    abreviar2 = 'BRL'

if event == 'Cancelar' or event == sg.WINDOW_CLOSED:
    window.close()
else:
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/{}-{}'.format(abreviar1, abreviar2))
    cotacoes = cotacoes.json()
    cotacoes = cotacoes['{}{}'.format(abreviar1, abreviar2)]['bid']
    sg.popup('Operação concluída!\nO valor de 1 {} em {} é de:'.format(moeda1, moeda2), cotacoes, title='')
