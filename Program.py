MonRate = int(input("What is the pokemon's default catch rate modifier?"))
Ball = input("What is the ball being used?")
match Ball:
    case "pokeball":
        BallRate = 1
    case "greatball":
        BallRate = 1.5
    case "ultraball":
        BallRate = 2
Health = int(input("What is the pokemon's health percentage?"))
Health = Health / 100
Status = input("What is the pokemon's status effect?")
if(Status == "sleep" or Status == "freeze"):
    StatusRate = 2.5
elif(Status == "paralyze" or Status == "poison" or Status == "burn"):
    StatusRate = 1.5
else:
    StatusRate = 1
CatchRate = ((MonRate*BallRate*StatusRate*(1-((2.0/3.0)*Health)))/255)*100
print(f"The current catch rate is {CatchRate}%")