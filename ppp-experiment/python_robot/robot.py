class Robot:
    forward =0
    backward=0
    lestside=0
    rightside=0

    def fwd(self,a):
        Robot.forward +=a
    
    def bwd(self,a):
        Robot.backward +=a
    
    def left(self,a):
        Robot.lestside +=a

    def right(self,a):
        Robot.rightside +=a

m=Robot()
m1=input("Switching:")
print("f-Forward\nb-Backward\nl-leftside\nr-rightside")

while m1 =="on":
    m2=input("enter the direction:")
    if m2=="f":
        a=int(input("enter the steps:"))
        m.fwd(a)
    elif m2=="b":
        a=int(input("enter the steps:"))
        m.bwd(a)
    elif m2=="l":
        a=int(input("enter the steps:"))
        m.left(a)
    elif m2=="r":
        a=int(input("enter the steps:"))
        m.right(a)
    elif m2 =="off":
        total_movements=Robot.forward+Robot.backward+Robot.lestside+Robot.rightside
        print("forward steps count:",Robot.forward)
        print("backward steps count:",Robot.backward)
        print("left steps count:",Robot.lestside)
        print("right steps count:",Robot.rightside)
        print("Total steps count:",total_movements)
        print("robot switching off")
        break
    else:
        print("sorry wrong command")
        
