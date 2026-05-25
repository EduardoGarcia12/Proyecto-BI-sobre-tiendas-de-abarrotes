print("proceso etl para raw sales")
print("hola mundo")

import pandas as pd
from datetime import datetime

datos = r"C:\Users\zabu\Desktop\abarrotes\raw_sales.xlsx"
limpios = r"C:\Users\zabu\Desktop\abarrotes\raw_sales_limpios.csv"

def etl_sl(datos, limpios):
    try: 
        #leemos el archivo 
        df = pd.read_excel(datos)
        
        #eliminamos duplicados 
        df = df.drop_duplicates()

        #validamos fechas

        df['sale_date'] = pd.to_datetime(df['sale_date'], utc=True)


        #validamos columnas numerics

        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
        df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
        df['discount_pct'] = pd.to_numeric(df['discount_pct'], errors='coerce')
        df['gross_amount'] = pd.to_numeric(df['gross_amount'], errors='coerce')
        df['discount_amount'] = pd.to_numeric(df['discount_amount'], errors='coerce')
        df['net_amount'] = pd.to_numeric(df['net_amount'], errors='coerce')

        #rellenamos si falta datos

        if df['quantity'].isnull().any():
            mean_q = df['quantity'].mean()
            df['quantity'] = (df['quantity'].fillna(mean_q).any()) 
        
        if df['unit_price'].isnull().any():
            mean_up = df['unit_price'].mean()
            df['unit_price'] = (df['unit_price'].fillna(mean_up).any())
        
        if df['discount_pct'].isnull().any():
            mean_dpc = df['discount_pct'].mean()
            df['discount_pct'] = (df['discount_pct'].fillna(mean_dpc).any())
        
        if df['gross_amount'].isnull().any():
            mean_gam = df['gross_amount'].mean()
            df['gross_amount'] = (df['gross_amount'].fillna(mean_gam).any())
        
        if df['discount_amount'].isnull().any():
            mean_damou = df['discount_amount'].mean()
            df['discount_amount'] = (df['discount_amount'].fillna(mean_damou).any())
        
        if df['net_amount'].isnull().any():
            mean_netamou = df['net_amount'].mean()
            df['net_amount'] = (df['net_amount'].fillna(mean_netamou).any())

        #guardamos el archivo excel

        df.to_csv(limpios, index=False, encoding= 'utf-8')
        
        #debugging 
        print(df.info())
        print("\nlos datos faltantes son: ")
        print(df.isnull().sum())
        print(f"\nlos datos procesados fueron: {len(df)}")

        return True
    
    except Exception as e: 
        print(f"hubo un error en el proceso etl: {e}")
        return False 

if __name__ == '__main__':
    etl_sl(datos, limpios)