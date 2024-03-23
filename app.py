import random

# Vamos a crear el juego piedra, papel o tijera con los siguientes requierimientos:
# Mensaje de bienvenida
print("Bienvenido al juego de piedra, papel o tijera")  

# El juego tiene que mostrar el número de rondas jugadas y el número de rondas ganadas por el jugador.
# Inicializar las variables de puntuación
rounds = 0
player_wins = 0

while True:
    
    # Mostrar el número de ronda actual
    print(f"\n######### Ronda {rounds + 1} #########")

    # El jugador puede elegir una de las tres opciones, o , y debe ser advertido si ingresa una opción no válida.
    player_choice = input("Elige piedra (r), papel (p) o tijera (s): ").lower()
    
    if player_choice not in ['r', 'p', 's']:
        print("Opción no válida. Por favor, elige nuevamente.")
        continue

    # La computadora elige aleatoriamente una opción
    computer_choice = random.choice(['r', 'p', 's'])

    # Determinar el resultado de la ronda
    if player_choice == computer_choice:
        print("¡Empate!")
        rounds += 1
    elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p'):
        print("¡Ganaste!")
        player_wins += 1
        rounds += 1
    else:
        print("¡Perdiste!")
        rounds += 1

    # Mostrar la elección de la computadora, si es r = piedra, si es p = papel, si es s = tijera
    if computer_choice == 'r':
        computer_choice = 'piedra'
    elif computer_choice == 'p':
        computer_choice = 'papel'
    else:
        computer_choice = 'tijera'

    print(f"La computadora eligió: {computer_choice}")

    # Mostrar la elección del jugador, si es r = piedra, si es p = papel, si es s = tijera
    if player_choice == 'r':
        player_choice = 'piedra'
    elif player_choice == 'p':
        player_choice = 'papel'
    else:
        player_choice = 'tijera'
        
    print(f"Tú elegiste: {player_choice}")    

    # Preguntar si el jugador quiere volver a jugar
    play_again = input("\n¿Quieres volver a jugar? (s/n): ").lower()
    if play_again != 's':
        break

# Muestra la puntuación del jugador al final del juego.
print(f"Rondas jugadas: {rounds}")
print(f"Rondas ganadas: {player_wins}")

# Mensaje de despedida
print("\nGracias por jugar!")
