print("hola mundo")
print("proceso etl para stores")

import pandas as pd
from datetime import datetime

datos=r"C:\Users\zabu\Desktop\abarrotes\stores.xlsx"
limpios=r"C:\Users\zabu\Desktop\abarrotes\stores_limpios.csv"


def etl_stores(datos, limpios):
    try: 
        #leemos el excel

        df = pd.read_excel(datos)

        #borramos duplicados 

        df = df.drop_duplicates()

        #validamos fechas 

        df['opening_date'] = pd.to_datetime(df['opening_date'], utc=True)

        #guardamos el csv

        df.to_csv(limpios, index=False, encoding='utf-8')
        return True
    
    except Exception as e: 
        print(f"Hubo un error en el proceso etl: {e}")
        return False

if __name__ == '__main__':
    etl_stores(datos, limpios)