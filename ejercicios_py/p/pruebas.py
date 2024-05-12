#  def load(self, filename):
#         try:
#             with open(filename, 'r', encoding='utf-8') as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     self.words.append(row[0].upper().strip()) #como las palabras están en la primera columna, usamos el indice 0
#                                                                 # ponemos las palabras en mayusculas y quitamos los espacios que puedan tener
#         except FileNotFoundError:
#             print("El archivo no se ha encontrado")
            
            
            
            
#  #Función que comprueba que se hayan cargado las 30 palabras como requisito para iniciar el juego       
#     def get_number_of_words(self):
#         if len(self.words) == 30:
#             return True
#         else:
#             return False

# img_hangman = [
#             """ 
#                 .______.
#                 |      |
#                 |      
#                 |     
#                 |     
#                 |
#               -----      
#             """,                      
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |     
#                 |     
#                 |
#               -----       
#             """,            
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |      |
#                 |      |
#                 |     
#               -----
#             """,
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |     \\|
#                 |      |
#                 |
#               -----      
#             """,
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |     \\|/
#                 |      |
#                 | 
#               -----      
#             """,         
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |     \\|/
#                 |      |
#                 |     / 
#               ----- 
#             """,
#             """
#                 .______.
#                 |      |
#                 |      O
#                 |     \\|/
#                 |      |
#                 |     / \\
#               -----      
#             """   
#         ]
# print(img_hangman[6])        
    
