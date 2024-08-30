from generator import Sprite
from generator import Anim

if __name__ == "__main__":
    code = 0
    
    while code != 3:
        print("==========================================")
        print("|                                        |")
        print("|   PNG SET GENERATOR                    |")
        print("|                                        |")
        print("==========================================")
        print('\n')

        print("    Select the function\n")
        print("  1. Sprite sheet Generation")
        print("  2. Animation set Generation")
        print("  3. Exit\n")

        code = int(input(" >>"))
        
        if code == 1:
          name = input("Enter the sprite sheet name >>")
          sprite = Sprite(name)
          sprite.generate()

        elif code == 2:
          name = input("Enter the animation set name >>")
          anim = Anim(name)
          anim.generate()

        elif code == 3: print("\nGENERATOR SHUT DOWN . . .\n")
        else: print("\nWRONG CODE!\n")