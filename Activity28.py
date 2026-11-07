class Badminton:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Badminton - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} smashes the shuttlecock with a thunderous force!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

            
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} kicks the ball with precision and power!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")


badminton = Badminton("Lin Dan", 67)
football = Football("Ronaldo", 10)

print("===== Sports Score Show =====\n")
for sport in [badminton, football]:
    sport.info()
    sport.play()
    print()


print("---Direct change attempt---")
badminton.__score = 100
print(f"get_score() still shows: {badminton.get_score()}")

print("\n--- Updating score ---")
badminton.set_score(100)
football.set_score(15)
