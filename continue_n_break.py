shopping_list = ["milk", "pasta", "eggs", "cheese", "bread", "rice"]
for item in shopping_list:
    if item == "eggs":
        print("I'm ignoring eggs")
        continue
    print(f"Buy {item}")  