
def userInput():
  """ en mayusculas! """
  departamento = input("Ingrese el departamento (opcional): ")
  municipio = input("Ingrese el municipio (opcional): ")
  cultivo = input("Ingrese el cultivo (opcional): ")

  filters = {}
  if departamento:
    filters["departamento"] = departamento.upper()
  if municipio:
    filters["municipio"] = municipio.upper()
  if cultivo:
    cultivo = cultivo.capitalize()
    filters["cultivo"] = cultivo

  return filters
