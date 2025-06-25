from tkinter import *;

def madlib1():
    animals = input("Enter a type of animal: ")
    profession=input("Enter a profession: ")
    cloth=input("Enter a piece of clothing: ")
    things=input("Enter a thing: ")
    name=input("Enter a name:  ")
    place = input("Enter a place: ")
    verb = input("EWnter a verb: ")
    food = input("Enter a food: ")

    print(f"Say {food}!” the photographer said as the camera flashed. {name} and I had gone to {place} to get our photos taken on my birthday. The first photo we really wanted was of us dressed as {animals}, pretending to be {profession}s. When we saw the proofs, I was a bit shocked — there were so many {things} in the background! I hadn’t imagined so many {cloth}s behind us. But the second photo was perfect. We both looked like {verb} superstars!")


def madlib2():
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place: ")
    person = input("Enter a person: ")
    adjective1 = input("Enter another adjective: ")
    insect = input("Enter an insect: ")
    food = input("Enter a food: ")
    verb = input("Enter a verb: ")

    print(f"Last night I dreamed I was a {adjective} butterfly with {color} wings that looked like {thing}. I flew to {place} with my best friend, {person}, who was a {adjective1} {insect}. We ate some {food} together and then decided to {verb}. It was the most magical dream ever.")


def madlib3():
    person = input("Enter a person's name: ")
    color = input("Enter a color: ")
    foods = input("Enter a food: ")
    adjective = input("Enter an adjective: ")
    things = input("Enter a thing: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    print(f"Today we picked apples from {person}’s orchard. I had no idea there were so many different colored apples — {color}, for example! We ate {foods} apple pies while {adjective} {things} sang songs in the background. It felt like we were in {place}. I went home and {verb} {adverb} for the rest of the day.")

# GUI Setup

root = Tk()
root.title("Mad Libs Game")
root.geometry("400x400")
root.config(bg="#FFF8DC")

title_font = ("Comic Sans MS", 22, "bold")
label_font = ("Georgia",16)
button_font = ("Helvetica", 12, "bold")

Label(root, text="🎉 Mad Libs Generator 🎉", font=title_font, bg="#FFF8DC", fg="#D2691E").pack(pady=10)

frame = Frame(root, bg="#FFF8DC")
frame.pack(pady=20)

Label(frame, text="Choose Your Adventure", font=label_font, bg="#FFF8DC", fg="#4B0082").pack(pady=5)



Button(frame, text="📸 Photo Shoot", font=button_font, command = madlib1, bg="#FFB6C1", fg="black", width=20, bd=2, relief=RAISED).pack(pady=10)
Button(frame, text="🌙 Dream World", font=button_font, command = madlib2, bg="#87CEFA", fg="black", width=20, bd=2, relief=RAISED).pack(pady=10)
Button(frame, text="🍎 Apple Orchard", font=button_font, command= madlib3, bg="#98FB98", fg="black", width=20, bd=2, relief=RAISED).pack(pady=10)

Label(root, text="Made with ♥ in Python", font=("Arial", 10), bg="#FFF8DC", fg="#555").pack(side=BOTTOM, pady=10)
root.mainloop()