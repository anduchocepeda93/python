lucky_numbers = [4, 15, 8, 16, 23, 42]
print(lucky_numbers)
friends = ["Ross", "Chandler", "Joey", "Phoebe", "Rachel", "Monica"]
friends[1] = "Gunther"
print(friends)
print(friends[1])

friends.extend(lucky_numbers)
print(friends)
friends.append("Gunther")   
print(friends)
friends.insert(1, "Gunther")    
print(friends)
friends.remove("Gunther")
print(friends)
friends.pop()
print(friends)
print(friends.index("Joey"))
print(friends.count("Gunther"))
friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)


lucky_numbers.sort()  
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

