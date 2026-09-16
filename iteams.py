iteams = ["Wand", "Rock", "Pogo stick"]
levels = [1,2,3]
for level in levels:
    for item in iteams:
        if level == 2 and item =="Rock":
            continue
        else:
            print(f"you can get a {item} at level {level}")
    
            