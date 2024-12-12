# Python Calculator API

## Popis
Tento projekt implementuje jednoduché REST API pro kalkulačku v Pythonu pomocí Flasku. API poskytuje čtyři základní matematické operace:

- Sčítání: `/add?a=1&b=2`
- Odčítání: `/subtract?a=5&b=3`
- Násobení: `/multiply?a=3&b=4`
- Dělení: `/divide?a=8&b=2`

API odpovídá ve formátu JSON.

## Funkce

- **Sčítání:** Přijímá dvě čísla a vrátí jejich součet.
- **Odčítání:** Přijímá dvě čísla a vrátí rozdíl.
- **Násobení:** Přijímá dvě čísla a vrátí jejich součin.
- **Dělení:** Přijímá dvě čísla a vrátí jejich podíl. Ošetřeno dělení nulou.

## Technologie

- Python 3.7+
- Flask
- Swagger UI (pro automatickou generovanou dokumentaci)
- Doctest (pro testování příkladů v docstringu)
- Sphinx (pro generování statické dokumentace)
- PlantUML (pro generování sekvenčního diagramu)

## Instalace

1. Klonujte tento repozitář:

   ```git clone https://github.com/uzivatel/python-calculator-api.git```\
   ```cd python-calculator-api```


3. Vytvořte virtuální prostředí a aktivujte ho:

   ```python -m venv venv```\
   ```source venv/bin/activate   # Na Linux/Mac```\
   ```venv\bin\activate      # Na Windows```


4. Nainstalujte závislosti:

   ```pip install -r requirements.txt```


5. Spustťe aplikaci:

   ```python src/app.py```


Aplikace poběží na http://localhost:5000.
