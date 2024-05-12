def imprime_lista_de_letras(letras, palabra):
  # letras = set(letras)
  palabra = palabra.upper()
  return ' '.join(['_' if l in letras else l for l in palabra])

def esta_palabra_completa(letras, palabra):
  for l in palabra:
    if l not in letras:
      return False