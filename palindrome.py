s = "a man, a plan, a canal: Panama"

def palindrome(apal):
    box = []
    delthis = ''
    for char in apal.lower():
        if char.isalpha():
            box.append(char)
    if delthis.join(reversed(box)) == delthis.join(box):
        return True, f'{delthis.join(box)} is a palindrome!'
    else:
        return False, f'{delthis.join(box)}is not a palindrome :('
                
        
print(palindrome(s))

# Well, this probably runs like a mack truck, but I won't lie im lowkey proud of myself for doing this one with
# no help from outside sources in a short amount of time. Feels good.
#I'm gunna guess since it went through a for loop and it being reversed, that would put it in O(n^2) territory.