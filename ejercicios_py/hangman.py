# import pandas as pd
import csv
import random

class Hangman:
    def __init__(self):
        self.words = []
        self.username = ''  
        self.current_word = ''
        self.num_rounds = 0  
        self.user_rounds = 5 
    
    def load(self, filename):   
        # Abre el archivo CSV en modo lectura
        with open(filename, mode='r', encoding='utf-8') as archivo_csv:
            # Crea un lector CSV
            lector_csv = csv.reader(archivo_csv)
            # Itera sobre las filas del archivo CSV
            for fila in lector_csv:
                self.words.append(fila[0])
                
    # Metodo para comprobar estan las 30 palabras
    def get_number_of_words(self):
        if len(self.words) == 30:
            print('¿Preparados para un nuevo reto?...A JUGAR!!')
            return True
        else:
            print('vaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego')
            return False
        
    # def jugar(self):    
    #     if self.get_number_of_words():
    #         print('¿Preparados para un nuevo reto?\nBienvenidos al AHORCADO!!')
    
    #         # Pedir nombre al usuario
    #         self.username = input('Nombre de usuario: ')
    #         print(f'Empieza el juego {self.username}!!')
    #     else:
    #         print('vaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego')

    # METODO: Elegir la palabra aleatoriamente
    def choose_word(self):
        
        self.current_word = random.choice(self.words)
    
    # METODO: Peticiones para comenzar el juego
    def start_game(self):
        
        self.username = input('Nombre de usuario: ')
        self.choose_word()
        print(f'¡¡Bienvenidos al AHORCADO!! \n{self.username} adivina la palabra: {'_ ' * len(self.word_to_guess)}')

    # METODO: construir rondas
    def play_round(self):
        print('Empieza la primera ronda')
        self.num_rounds = 0
        used_letters = set()
        while True:
            letter = input('Introduce una letra: ').upper()
            # isalpha() determina si todos los caracteres de
            # la cadena son alfabéticos
            if letter.isalpha() and letter == 1:
                if letter in used_letters:
                    print(f'ERROR. La letra {letter} ya la has utilizado.')
                
            if letter in self.current_word:
                
            
            
    # METODO: Contiene las imágenes de los estados del ahorcado
    def print_hangman(self):
        img_hangman = [
            """ 
                .______.
                |      |
                |      
                |     
                |     
                |
              -----      
            """,                      
            """
                .______.
                |      |
                |      O
                |     
                |     
                |
              -----       
            """,            
            """
                .______.
                |      |
                |      O
                |      |
                |      |
                |     
              -----
            """,
            """
                .______.
                |      |
                |      O
                |     \\|
                |      |
                |
              -----      
            """,
            """
                .______.
                |      |
                |      O
                |     \\|/
                |      |
                | 
              -----      
            """,         
            """
                .______.
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
              ----- 
            """,
            """
                .______.
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
              -----      
            """   
        ]
        print(img_hangman(self.num_rounds))
# resultado = hangman1.choose_word        

# Pruebas 
# hangman1 = Hangman()
# hangman1.load('./ficheros/words.csv')
# print(hangman1.choose_word())
# print(hangman1.current_word)

# if hangman1.get_number_of_words():
#     username = input("Introduce tu nombre de usuario: ")
#     word_to_guess = hangman1.current_word
#     print(f"¡Bienvenido {username}! Adivina la palabra: {'_ ' * len(word_to_guess)}")

    