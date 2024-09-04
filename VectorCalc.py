import math

# The angle is entered by the angle from the positive x axis with anything in the negative y axis is in negative degrees from positive x axis.
# if the force is going outwards (away from origo) it is positive and if it's pointed towards origo it's negative

RepsQuestions = 0
RepsComponents = 0
TotComponentX = 0
TotComponentY = 0
Vectors = []
VectorsDeg = []
ComponentX = []
ComponentY = []

NumberOfVectors = input("How many vectors do you want to calculate: ")

#Appends input to lists, the pair of Vector and Angle of said Vector has the same index in the two different lists
while RepsQuestions < int(NumberOfVectors):
    Vectors.append(input(f"Force of vector {RepsQuestions+1}: "))
    VectorsDeg.append(input(f"Angle of vector {RepsQuestions+1} in degrees: "))
    RepsQuestions = RepsQuestions + 1
    print("-"*25)

#Calculates the components of all vectors
for CurrentVector in Vectors:
    ComponentX.append(float(CurrentVector) * math.cos(math.radians(float(VectorsDeg[RepsComponents]))))
    ComponentY.append(float(CurrentVector) * math.sin(math.radians(float(VectorsDeg[RepsComponents]))))
    RepsComponents = RepsComponents + 1

#Sums the components in both x and y directions
for CurrentComponentX in ComponentX:
    TotComponentX = TotComponentX + CurrentComponentX

for CurrentComponentY in ComponentY:
    TotComponentY = TotComponentY + CurrentComponentY

print(f"Total forces in X direction: {TotComponentX}")
print(f"Total forces in Y direction: {TotComponentY}")
print("-"*25)

#Calculates the resultant and angle of the resultant
Resultant = math.sqrt(TotComponentX ** 2 + TotComponentY ** 2)
print(f"Resultant: {Resultant}")

ResultantAngle = math.degrees(math.atan2(TotComponentY, TotComponentX))
print(f"Resultant angle in degrees: {ResultantAngle}")  
