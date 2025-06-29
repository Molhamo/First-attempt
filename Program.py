MonRate = int(input("What is the pokemon's default catch rate modifier?"))
BallRate = int(input("What is the ball's catch rate multiplier?"))
Health = int(input("What is the pokemon's health percentage?"))
Health = Health / 100
StatusRate = int(input("What is the catch rate multiplier from status effects?"))
CatchRate = ((MonRate*BallRate*StatusRate*(1-((2.0/3.0)*Health)))/255)*100
print(f"The current catch rate is {CatchRate}%")