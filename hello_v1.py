""" Hello Word em diferentes linguas.

Dependendo da lingua configurada no ambiente o programa usa a lingua
correspondente

Como usar: 
    Tenha a variavel LANG devidamente configurada

    export LANG=pt_BR
Execução: 
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.2"
__author__ =  "Aline Costa"
__lincese__ = "Unlicense"

import os 

list_current_language = {
    "en_US" : "Hello, World!",
    "pt_BR" : "Olá, Mundo!",
    "it_IT" : "Cia, Mondo!"
}

current_language = os.getenv("LANG", "en_US")[:5] #Caso não exista, usar a ligua inglesa e pegue somente os primeiros 5 caracteres para não retornar "en_US.utf8"

print(list_current_language[current_language])
