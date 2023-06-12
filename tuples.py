# A tuple is a collection datatype that is already ordered and unchangeable/imutable after creation. 
# They are used to store multiple items in a single variable.

mytuple = ("Akos", 23, "Avocado")

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[::-1]
print(b)

# Given thte tuple belwo that represents the Imelda May track "More Mayhen",
# write code to print the album details, followed by a listing of all the tracks in 
# the album.
# 
# Indent the tracks by a single tab stop when printing then (remember that you
# can pass mor than one item to the print function, separating them with a coma).

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayham"),(4, "KEntish Town Waltz"))

title, album, year, tracks = imelda
print(imelda)

print("=" *100)
print(title)
print(album)
print(year)
for songs in tracks:
    tracks, titile = songs
    print(f"\tTrack number {tracks}, Title: {title}")
