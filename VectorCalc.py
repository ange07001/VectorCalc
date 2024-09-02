import math

RepsQuestions = 0
RepsComponents = 0
TotComponentX = 0
TotComponentY = 0
Vectors = []
VectorsDeg = []
ComponentX = []
ComponentY = []

NumberOfVectors = input("How many vectors do you want to calculate: ")

while RepsQuestions < int(NumberOfVectors):
    Vectors.append(input(f"Force of vector {RepsQuestions+1}: "))
    VectorsDeg.append(input(f"Angle of vector {RepsQuestions+1} in degrees: "))
    RepsQuestions = RepsQuestions + 1
    print("-"*25)

for CurrentVector in Vectors:
    ComponentX.append(float(CurrentVector) * math.cos(math.radians(float(VectorsDeg[RepsComponents]))))
    ComponentY.append(float(CurrentVector) * math.sin(math.radians(float(VectorsDeg[RepsComponents]))))
    RepsComponents = RepsComponents + 1

for CurrentComponentX in ComponentX:
    TotComponentX = TotComponentX + CurrentComponentX

for CurrentComponentY in ComponentY:
    TotComponentY = TotComponentY + CurrentComponentY

print(f"Total forces in X direction: {TotComponentX}")
print(f"Total forces in Y direction: {TotComponentY}")
print("-"*25)

Resultant = math.sqrt(TotComponentX ** 2 + TotComponentY ** 2)
print(f"Resultant: {Resultant}")

ResultantAngle = math.degrees(math.atan2(TotComponentY, TotComponentX))
print(f"Resultant angle in degrees: {ResultantAngle}")  
