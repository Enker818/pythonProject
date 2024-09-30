import random
import threading


def dart(player_number):
    total_score = 0
    print(f"Spiller {player_number}")
    for kast in range(1, 4):
        poeng = random.randrange(0, 61)
        total_score += poeng
        print(f"Kast {kast}: fikk {poeng} poeng")

    print(f"Spiller {player_number} fikk totalt {total_score} poeng\n")


threads = []

antall = int(input("hvor mange spillere skal spilles?"))

for i in range(1, antall + 1):
    t = threading.Thread(target=dart, args=(i,))
    t.daemon = True
    threads.append(t)


for t in threads:
    t.start()


for t in threads:
    t.join()
