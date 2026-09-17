def get_doneness(temp):
 
    temp= 165
    if temp <= 125:
        print("Rare")
        if temp >= 135:
            print("medium rare")
       
    
    

# ---------- DO NOT modify below this line ----------
print(get_doneness(125))
print(get_doneness(135))
print(get_doneness(145))
print(get_doneness(155))
print(get_doneness(165))
