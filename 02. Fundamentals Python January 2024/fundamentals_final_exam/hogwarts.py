spell = input()


def abjuration():
    global spell
    spell = spell.upper()
    print(spell)


def necromancy():
    global spell
    spell = spell.lower()
    print(spell)


def illusion(index, letter):
    global spell
    if 0 <= index < len(spell):
        spell = spell[:index] + letter + spell[index + 1:]
        print("Done!")
    else:
        print("The spell was too weak.")


def divination(first_substring, second_substring):
    global spell
    if first_substring in spell:
        spell = spell.replace(first_substring, second_substring)
        print(spell)


def alteration(substring):
    global spell
    if substring in spell:
        spell = spell.replace(substring, "")
        print(spell)


while True:
    command = input().split()
    if command[0] == "Abracadabra":
        break

    if command[0] == "Abjuration":
        abjuration()
    elif command[0] == "Necromancy":
        necromancy()
    elif command[0] == "Illusion":
        illusion(int(command[1]), command[2])
    elif command[0] == "Divination":
        divination(command[1], command[2])
    elif command[0] == "Alteration":
        alteration(command[1])
    else:
        print("The spell did not work!")
