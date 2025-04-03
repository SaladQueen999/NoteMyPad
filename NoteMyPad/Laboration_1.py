# 1 c = 8 oz.
# läser in antal cups och ounzes per portion + abtal portioner
#räkna antalet cups och ounzes för det givna portionen
cups = int(input("Number of cups: "))
oz = int(input("Number of oz: "))
servings = int(input("Number of servings: "))
totalCups = cups * servings
totalOz = oz * servings
extraCups = totalOz // 8
newOz = totalOz % 8
totalCups += extraCups
print (f'{totalCups} c {newOz} oz')