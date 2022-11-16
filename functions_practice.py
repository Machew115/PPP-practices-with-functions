def hello():
    print("hello user")
hello()
def pack(a, b, c):
    return [a, b, c]

print(pack(1, 2, 3)) 

def eatlunch(food):
    if len(food) == 0:
        print("My Lunch Box is Empty")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"first I eat {food[0]}")
            else:
                print(f"next I eat{food[i]}")

eatlunch([])
eatlunch(["sandwich, apple, banana"])
eatlunch(["apple","banana","sandwich","cookie"])