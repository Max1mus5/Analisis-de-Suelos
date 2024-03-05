import numpy as np
import pandas as pd

def eliminar_caracteres_especiales(data):
    try:
        data['potasio_k_intercambiable_cmol_kg'] = data['potasio_k_intercambiable_cmol_kg'].str.replace('[<>]', '', regex=True)
        data['f_sforo_p_bray_ii_mg_kg'] = data['f_sforo_p_bray_ii_mg_kg'].str.replace('[<>]', '', regex=True)
        data['ph_agua_suelo_2_5_1_0'] = data['ph_agua_suelo_2_5_1_0'].str.replace('[<>]', '', regex=True)
        return data
    except Exception as e:
        print(f"Error al eliminar caracteres especiales: {str(e)}")
        return None
    
def cambiar_coma_por_punto(data):
    try:
        data['potasio_k_intercambiable_cmol_kg'] = data['potasio_k_intercambiable_cmol_kg'].str.replace(',', '.', regex=True)
        data['f_sforo_p_bray_ii_mg_kg'] = data['f_sforo_p_bray_ii_mg_kg'].str.replace(',', '.', regex=True)
        data['ph_agua_suelo_2_5_1_0'] = data['ph_agua_suelo_2_5_1_0'].str.replace(',', '.', regex=True)
        return data
    except Exception as e:
        print(f"Error al cambiar la coma por punto: {str(e)}")
        return None
    
def reemplazar_nd_mi_por_nan(data):
    try:
        data['potasio_k_intercambiable_cmol_kg'] = data['potasio_k_intercambiable_cmol_kg'].replace(['ND', 'MI'], np.nan)
        data['f_sforo_p_bray_ii_mg_kg'] = data['f_sforo_p_bray_ii_mg_kg'].replace(['ND', 'MI'], np.nan)
        data['ph_agua_suelo_2_5_1_0'] = data['ph_agua_suelo_2_5_1_0'].replace(['ND', 'MI'], np.nan)
        return data
    except Exception as e:
        print(f"Error al reemplazar 'ND' por nan: {str(e)}")
        return None
    
def normalizar(data):
    try:
        # Reemplazar '..' por '.' 
        data['potasio_k_intercambiable_cmol_kg'] = data['potasio_k_intercambiable_cmol_kg'].replace('..', '.', regex=True)
        data['f_sforo_p_bray_ii_mg_kg'] = data['f_sforo_p_bray_ii_mg_kg'].replace('..', '.', regex=True)
        data['ph_agua_suelo_2_5_1_0'] = data['ph_agua_suelo_2_5_1_0'].replace('..', '.', regex=True)
        return data
    except Exception as e:
        print(f"Error al normalizar los datos: {str(e)}")
        return None
    
   
    
def convertir_a_numeros(data):
    try:
        data['potasio_k_intercambiable_cmol_kg'] = pd.to_numeric(data['potasio_k_intercambiable_cmol_kg'].astype(float))
        data['f_sforo_p_bray_ii_mg_kg'] = pd.to_numeric(data['f_sforo_p_bray_ii_mg_kg'].astype(float))
        data['ph_agua_suelo_2_5_1_0'] = pd.to_numeric(data['ph_agua_suelo_2_5_1_0'].astype(float))
        return data
    except Exception as e:
        print(f"Error al convertir a números: {str(e)}")
        return None
    
def eliminar_valores_nulos(data):
    try:
        data['potasio_k_intercambiable_cmol_kg'] = data['potasio_k_intercambiable_cmol_kg'].fillna(np.nan)
        data['f_sforo_p_bray_ii_mg_kg'] = data['f_sforo_p_bray_ii_mg_kg'].fillna(np.nan)
        data['ph_agua_suelo_2_5_1_0'] = data['ph_agua_suelo_2_5_1_0'].fillna(np.nan)
        return data
    except Exception as e:
        print(f"Error al eliminar valores nulos: {str(e)}")
        return None

def calcular_mediana_edaficas(data):
    try:
        #reemplazar 'ND' por nan
        data = reemplazar_nd_mi_por_nan(data)
        
        #eliminar caracteres especiales
        data = eliminar_caracteres_especiales(data)

        #cambiar "," por "."
        data = cambiar_coma_por_punto(data)      

        #marcar como nan
        data = eliminar_valores_nulos(data) 

        #cambiar a float
        data = convertir_a_numeros(data)

        #eliminar filas con valores nulos
        data = data.dropna(subset=['f_sforo_p_bray_ii_mg_kg', 'ph_agua_suelo_2_5_1_0', 'potasio_k_intercambiable_cmol_kg'])  # último filtro para evitar errores inesperados

        mediana_edaficas = data[['f_sforo_p_bray_ii_mg_kg', 'ph_agua_suelo_2_5_1_0', 'potasio_k_intercambiable_cmol_kg']].apply(lambda x: np.median(x), axis=0)

        return mediana_edaficas

    except Exception as e:
        print(f"Error al calcular la mediana de las variables edáficas: {str(e)}")
        return None
