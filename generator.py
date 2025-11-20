
from art1 import Art1
from art2 import Art2
from art3 import Art3
from art4 import Art4
from art5 import Art5
from art6 import Art6
from art7 import Art7
from art8 import Art8
from art9 import Art9

class ArtGenerator:
    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

        classes = {
            1: Art1, 2: Art2, 3: Art3,
            4: Art4, 5: Art5, 6: Art6,
            7: Art7, 8: Art8, 9: Art9
        }

        if choice in classes:
            classes[choice]().draw()
        else:
            print("Invalid choice")
