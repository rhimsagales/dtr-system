colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

print("The list below shows all the 7 colors in rainbow: \n{colors}\n")

colors.insert(0, 'Teal')
colors.insert(3, 'Pink')
print(f"Added new colors in the list: \n{colors}\n")


colors.insert(9, 'Pink')
colors.insert(10, 'Brown')
print(f"Added new colors in the list again: \n{colors}\n")


colors.pop(7)
print(f"Remove one color in the list: \n{colors}\n")


colors.pop(9)
print(f"Remove another color in the list: \n{colors}\n")

colors.sort()
print(f"Arrange color names in the list alphabetically and its corrent lenght: \n{colors} - {len(colors)}")


        
def duplicateFinder(varList):
    tempItems = []
    returnDup = []
    for item in varList:
        if item not in tempItems:
            tempItems.append(item)
        elif item not in returnDup:
            if item in returnDup:
                pass
            else:
                returnDup.append(item)
    return returnDup

occurences = [color for color in colors if colors.count(color) > 1]
    
print(f"Display the color name with duplicates and the number of times: \n{duplicateFinder(colors)} - {len(occurences)}\n")       