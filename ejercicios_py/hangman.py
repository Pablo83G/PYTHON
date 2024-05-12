# import pandas as pd
import csv
import random

class Hangman:
    def __init__(self):
        self.words = []
        self.username = ''  
        self.current_word = ''
        self.word_to_guess = ''
        self.rounds = 3 
        self.score = 0 
        self.letter = ''
        self.victory = False
        self.used_letters = set()
        self.right_letters = set()
    
    def load(self, filename):   
        try:
        # Abre el archivo CSV en modo lectura
            with open(filename, mode='r', encoding='utf-8') as archivo_csv:
            # Crea un lector CSV
                lector_csv = csv.reader(archivo_csv)
            # Itera sobre las filas del archivo CSV
                for fila in lector_csv:
                    self.words.append(fila[0].upper())
        except FileNotFoundError:
            print("El archivo no se ha encontrado")
                
    # Metodo para comprobar estan las 30 palabras
    def get_number_of_words(self):
        if len(self.words) == 30:
            return True
        else:
            return False
        

    # METODO: Elegir la palabra aleatoriamente
    def choose_word(self):
        self.current_word = random.choice(self.words)
        self.words.remove(self.current_word)
        #quitamos la palabra de la lista para evitar que se 
        # vuelva a escoger en la misma partida
        # print(self.current_word)
    
    
    # METODO: Peticiones para comenzar el juego
    def start_game(self):
        self.username = ''
        self.user_rounds = 0

        if(self.get_number_of_words()):
            print(f'¡¡Bienvenidos al AHORCADO!!')
            self.username = input('Introduce tu nombre de usuario: ')
            print(f'{self.username} adivina la palabra:')
            
            # Numero de rondas
            for round in range(self.rounds):
                self.user_rounds = round + 1
                print(f'Estas en la ronda {self.user_rounds}')
                self.play_round()
                # self.register_round('./files/rounds_in_games.csv')
            
            # Punttuación final
            print(f'FIN DEL JUEGO. {self.username} tu puntuación final es {self.score}')

            # Fecha de finalizacion
            # self.end_date()
                   
            #Registramos los datos de la partida en el fichero games.csv
            # self.register_game('./files/games.csv')
            
        else: 
            print('vaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego')
            
            
            
    # METODO: construir rondas
    def play_round(self):
        print()
        self.max_tries = 6
        self.tries = 0
        self.used_letters = set()
        self.victory = ''
        self.choose_word()
        # self.right_letters = set()
        while True:
            self.print_word_progress()
            self.print_hangman()
            print()
            self.letter = input('Introduce una letra: ').upper()
            
            print()
            # isalpha() determina si todos los caracteres de
            # la cadena son alfabéticos
            
            if self.letter.isalpha() and len(self.letter) == 1:
                
                if self.letter in self.used_letters:
                    print(f'ERROR. La letra {self.letter} ya la has utilizado.')
                    # mostrar lista de letras??
                    print('Estas son las letras que has utilizado: ' + ' '.join(self.used_letters))
                    print()
                    continue
                self.used_letters.add(self.letter)
                
                if self.letter in self.current_word:
                    print('¡Bien! has acertado.')
                    
                    if self.complete_word(self.used_letters):
                        print(f'¡¡ENHORABUENA {self.username.upper()} has ganado la ronda!!')
                        print(f'La palabra oculta es {self.current_word}')
                        if self.max_tries == self.tries:
                            print(f'No has utilizado ningún intento')
                            print()
                        else:    
                            print(f'Has utilizado {self.tries} intentos')
                            print()
                        self.score += 1
                        self.victory = True
                        break
                    
                    
                    else:
                        print(f'Te quedan {self.max_tries - self.tries} intentos.')
                        print('Estas son las letras que has utilizado: ' + ' '.join(self.used_letters))
                        print()
                        self.used_letters.add(self.letter)
                    
               
                else:
                    self.used_letters.add(self.letter)
                    self.tries += 1
                    print(f'OOhh. La palabra no contiene la letra {self.letter}\nVuelve a intentarlo')
                    print(f'Te quedan {self.max_tries - self.tries} intentos.')
                    print('Estas son las letras que has utilizado: ' + ' '.join(self.used_letters))
                    print()
                    
                    if self.tries == 6:
                        self.print_hangman()
                        print(f'GAME OVER!! Lo siento {self.username} has superado el máximo de intentos perimitidos')
                        print(f'La palabra oculta es {self.current_word}')
                        print()
                        self.victory = True
                        break
        
            else: 
                print('ERROR. Tienes que introducir una letra')
                print()        
                
                    
                
            
    # METODO: sustituir espacios por letras en la palabra oculta
    def print_word_progress(self):
        self.current_word = self.current_word.upper()
        return print(' '.join([l if l in self.used_letters else '_' for l in self.current_word]))

       
    # METODO: 
    
    
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
        print(img_hangman[self.tries])
        
    def complete_word(self, used_letters):
        for letter in self.current_word:
            if letter not in used_letters:
                return False
        return True
# resultado = hangman1.choose_word        

# Pruebas 
hangman_game = Hangman()
hangman_game.load('./ficheros/words.csv')
if hangman_game.get_number_of_words():
    hangman_game.start_game()
# print(hangman1.choose_word())
# print(hangman1.current_word)

# if hangman1.get_number_of_words():
#     username = input("Introduce tu nombre de usuario: ")
#     word_to_guess = hangman1.current_word
#     print(f"¡Bienvenido {username}! Adivina la palabra: {'_ ' * len(word_to_guess)}")

    