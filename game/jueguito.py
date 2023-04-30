import random
import os

def main():
        def clear_screen():
            os.system('clear')

        def the_options():
            
            options = ('piedra', 'papel', 'tijera')
            my_option = input('Elige PIEDRA, PAPEL O TIJERA: ').lower().strip()
            if not my_option in options:
                print('Opcion incorrecta, prueba de nuevo.')
                return None, None
                    
            cpu_option = random.choice(options)

            print(f'Mi opcion: {my_option}')
            print(f'Opcion de la CPU: {cpu_option}')

            return my_option, cpu_option


        def game_logic(my_option, cpu_option, my_wins, cpu_wins):

            if my_option == cpu_option:
                print('EMPATE!')

            elif my_option == 'piedra':
                if cpu_option == 'tijera':
                    print('Ganaste!!')
                    my_wins += 1
                else:
                    print('La CPU ganó!')
                    cpu_wins += 1
                        
            elif my_option == 'papel':
                if cpu_option == 'piedra':
                    print('Ganaste!!')
                    my_wins += 1
                else:
                    print('La CPU ganó!')
                    cpu_wins += 1

            elif my_option == 'tijera':
                if cpu_option == 'papel':
                    print('Ganaste!!')
                    my_wins += 1
                else:
                    print('La CPU ganó!')
                    cpu_wins += 1
                
            return my_wins, cpu_wins


        def game_start():
            my_wins = 0
            cpu_wins = 0
            round = 0
            
            while True:

                clear_screen()
                print('BIENVENIDO AL JUEGO DE PIEDRA, PAPEL Y TIJERA!')
                print()
                print('TURNO', round)
                print()
                print('computer wins:', cpu_wins)
                print('my wins:', my_wins)

                my_option, cpu_option = the_options()

                my_wins, cpu_wins = game_logic(my_option, cpu_option, my_wins, cpu_wins)

                if cpu_wins == 3:
                    print('El ganador es la CPU')
                    input('Presiona Enter para continuar.')
                    clear_screen()
                    break

                elif my_wins == 3:
                    print('El ganador es el usuario')
                    input('Presiona Enter para continuar.')
                    clear_screen()
                    break
                
                input('Presiona Enter para continuar')
                round += 1


        game_start()    

    
        



if __name__ == '__main__':
    main()