print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Bem vindo à Ilha do Tesouro')
print('Sua missão é encontrar o tesouro.')
first_option = input('Você está em uma cruzilhada. Onde você deseja ir? Digite "esquerda" ou "direita" ').lower()
if first_option == "esquerda":
    second_option = input('Você chegou à um lago. No meio do lago há uma ilha. Digite "esperar" para esperar por um barco. Digite "nadar" para nadar para lá. ').lower()
    if second_option == "esperar":
        third_option = input("Você chegou na ilha sem nenhum arranhão. Nela, há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul, qual cor você escolhe abrir? ").lower()
        if third_option == "azul":
            print("Você entrou numa sala cheia de monstros. Fim de jogo.")
        elif third_option == "vermelha":
            print("É uma sala cheia de fogo. Fim de jogo.")
        elif third_option == "amarela":
            print("Você encontrou o tesouro! Você venceu!")
    else:
        print("Você foi atacado por um salmão raivoso. Você morreu.")
else:
    print("Você caiu em um buraco, Fim de jogo.")
