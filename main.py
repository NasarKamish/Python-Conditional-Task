"""Getting the speed of the car and road adn storing them"""

RoadSpeed = int(input("Enter the road speed: "))
CarSpeed = int(input("Enter the speed of the car: "))

# we make the points 0 and increase it if need to
Points = 0
if CarSpeed < RoadSpeed:
    print("OK")
else:
    while CarSpeed > RoadSpeed:
        CarSpeed -= 5
        Points += 1
    print("Points: " + str(Points))
    if Points > 12:
        print("Time to go to jail!")
