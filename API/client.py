import pandas as pd
from sodapy import Socrata   

def get_data(departamento=None, municipio=None, cultivo=None, limit=None):

  client = Socrata('www.datos.gov.co',
                  'HGI4bbHPPjHjc5ZZ0wILVha8S',
                  username="j.riveros1@utp.edu.co",
                  password="7E1088ro239515?")

  params = {}
  if departamento:
    params["departamento"] = departamento
  if municipio:
    params["municipio"] = municipio
  if cultivo:
    params["cultivo"] = cultivo

  print(params)
  results = client.get("ch4u-f3i5", limit=limit, **params)

  # Convertir resultados a DataFrame
  results_df = pd.DataFrame.from_records(results)
  return results_df

