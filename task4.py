
"""
ANSWER BOX - Copy the strings you need:

"standing up or flopped down?"
") Keep it round.\n"
") Attach two pieces using {color2} hanging downward.\n"
") Name this creation: "Dog""
") Roll a smaller ball using {color1} for the head.\n"
"hot dog or round like a ball?"
") Roll a ball using {color1} for the body.\n"
") Attach two pointed pieces using {color2} upright.\n"
") Attach the head to the body.\n"
") Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n"
") Stretch it out.\n"
"""

def main():
    color1 = "blue"
    color2 = "pink"
    print(f"1) Roll a ball using {color1} for the body. \n ")
    choice1 = input("long or round? ")
    if choice1 == "round":
        print(f"2) keep it round. \n")
    else:
        print("2) stretch it out. \n")
    print(f"3) roll a smaller ball using {color1} for the head. \n")
    print("4) attach the head to the body. \n")
    choice2 = input("standing up or flopped down? ")
    if choice2 == "flopped down": 
        print(f"5) attach two pieces using {color2} hanging downward. \n")
    else: 
        print(f"5) attach two pieces using {color2} upright.\n ")
    print(f"6) add four legs using {color1}, a small tail using {color2}, two eyes, and a nose. \n")
    print('7) Name this creation: "dog" ')


if __name__ == "__main__":
    main()
