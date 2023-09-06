# Dictionary: Key-value pairs, unordered, mutable/cam be changed after creation

mydict = {"Mon": "Monday",
          "Tues": "Tuesday",
          "Wed": "Wednesday",
          "Thurs": "Thursday",
          "Fri": "Friday",
          "Sat": "Saturday",
          "Sun": "Sunday"}

# print(mydict)

# mydict["Sun"] = "Sunday"
# print(mydict)

# del mydict["Mon"]  # removing an item from a dictionary
# print(mydict)

while True:
    dict_key = input("Please enter a day: ")
    if dict_key == "quit":
        break
    if dict_key in mydict:
        description = mydict.get(dict_key)
        print(description)
    else:
        print(f"We don't have a {dict_key}")

