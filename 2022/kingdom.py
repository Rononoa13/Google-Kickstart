vowels_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def kingdom_names(names):

    kingdom_last_char = names[-1]
    """
    Checks if any character in vowels_list  
    is in the string kingdom_last_char
    """
    return kingdom_last_char

def get_ruler(names):

    if kingdom_names(names) == "y" or kingdom_names(names) == "Y":
        return names + " is ruled by nobody."

    kingdom_contains_vowel = any(
        vowels_list in kingdom_names(names) for vowels_list in vowels_list
    )
    if kingdom_contains_vowel:
        return names + " is ruled by Alice"
    else:
        return names + " is ruled by Bob"


print(get_ruler("Mollarist"))
