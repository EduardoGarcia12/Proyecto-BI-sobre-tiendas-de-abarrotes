print("proceso etl para inventory")

import pandas as pd
from datetime import datetime

datos = r"C:\Users\zabu\Desktop\abarrotes\inventory.xlsx"
limpios = r"C:\Users\zabu\Desktop\abarrotes\inventory_limpios.csv"

def etl_inventory(datos, limpios):
    try: 
        #leemos el excel
        df = pd.read_excel(datos)

        #eliminamos duplicados

        df = df.drop_duplicates()

        #validamos fechas

        df['last_update'] = pd.to_datetime(df['last_update'], utc=True)

        #validamos columnas numericas 

        df['store_id'] = pd.to_numeric(df['store_id'], errors='coerce')
        df['product_id'] = pd.to_numeric(df['product_id'], errors='coerce')
        df['stock_quantity'] = pd.to_numeric(df['stock_quantity'], errors='coerce')
        df['reorder_level'] = pd.to_numeric(df['reorder_level'], errors='coerce')

        #rellenamos valores faltantes 

        if df['stock_quantity'].isnull().any():
            mean_s_q = df['stock_quantity'].mean()
            df['stock_quantity'] = (df['stock_quantity'].fillna(mean_s_q).any())

        if df['reorder_level'].isnull().any():
            mean_r_l = df['reorder_level'].mean()
            df['reorder_level'] = (df['reorder_level'].fillna(mean_r_l).any())
        
        #guardamos el csv

        df.to_csv(limpios, index=False, encoding='utf-8')

        print(df.info())
        print("\nvalores nulos")
        
        print(df.isnull().sum())
        print(f"\nlos datos procesados fueron: {len(df)}")

        return True
    
    except Exception as e:
        print(f"hubo un error en el proceso etl: {e}")
        return False

if __name__ == '__main__':
    etl_inventory(datos, limpios)