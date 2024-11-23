import blackjack_module as bjm


#Funksjon for å skrive ut resultatet etter en runde
def print_result(player_verdi, dealer_verdi, bet, chips):
    if dealer_verdi > 21:
        print("Du vant!")
        chips += bet
    elif player_verdi > dealer_verdi:
        print("Dealer tapte! du vant!")
        chips += bet
    elif dealer_verdi > player_verdi:
        print("Du Tapte! Dealer vant.")
        chips -= bet
    else:
        print("Uavgjort!")

    print(f"dine chips: {chips}")
    return chips


#Funksjon for å spille en runde med Blackjack
def play_blackjack_round(chips):
    # 1.2.1 Validating bet
    while True:
        try:
            bet = int(input(f"plasere bette dit (Du har {chips} chips): "))
            if bet <= 0 or bet > chips:
                print("Du må plasere minst en et chips eller ikke mer enn det du har.")
            else:
                break
        except verdiError:
            print("Tast in en tall.")

    # 1.2.2 setupen for runden
    deck = bjm.get_new_shuffled_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    player_verdi = bjm.calculate_hand_value(player_hand)
    dealer_verdi = bjm.calculate_hand_value([dealer_hand[0]])

    print(f"\nKorte er delt ut. Du har en {player_hand[0]} Og {player_hand[1]}, og har totalt {player_verdi} verdi.")
    print(f"dealers sitt kort er {dealer_hand[0]}, og har totalt {dealer_verdi} verdi.")

    # runden
    if player_verdi == 21:
        print("Gratis du Vant blackjack")
        chips += bet * 2
        print(f"Dine chips: {chips}")
        return chips

    #spiller sin tur
    while player_verdi <= 21:
        choice = input("Hvis du vil hite tast in 1 eller 2 for Stand? ")

        if choice == "1":
            player_hand.append(deck.pop())
            player_verdi = bjm.calculate_hand_value(player_hand)
            print(f"Din nye kort er {player_hand} Med totalt {player_verdi} verdi.")
            if player_verdi > 21:
                print("Du tapte.")
                chips -= bet
                print(f"Dine chips: {chips}")
                return chips
        elif choice == "2":
            print(f"\ndealers nye kort er {dealer_hand} Med totalt {bjm.calculate_hand_verdi(dealer_hand)} verdi.")
            print(f"Din kort er {player_hand} Og har antall {player_verdi} verdi.")
            # 1.2.5 Dealer's turn to draw cards
            while bjm.calculate_hand_verdi(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            dealer_verdi = bjm.calculate_hand_verdi(dealer_hand)
            print(f"dealer's siste kort {dealer_hand} Og har antall {dealer_verdi_verdi} verdi.")


            chips = print_result(player_verdi, dealer_verdi, bet, chips)
            return chips

    return chips


#Funksjon for å spørre spilleren om å spille en ny runde eller avslutte
def ask_to_play_again(chips):
    if chips <= 0:
        print("Du tapte dine chips.")
        restart = input("Vil du spille igjen? (y/n): ").lower()
        if restart == 'y':
            print("\nRestarter spillet...\n")
            return 5  #reseter chip for nye spill
        else:
            print("Velkommen tilbake!")
            return 0  #
    else:
        play_again = input("Vil du spille enda enn runde (yes/klikk enter): ").lower()
        if play_again == "yes":
            return chips
        else:
            print("Thanks for playing!")
            return 0



def play_blackjack():
    chips = 5  #Start chips

    while chips > 0:
        chips = play_blackjack_round(chips)


        chips = ask_to_play_again(chips)
        if chips == 0:
            break


if __name__ == "__main__":
    play_blackjack()
