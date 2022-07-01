import random


s = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
storage = [p,s,r]
player = input("輸入你出了啥s(剪刀)/r(石頭)/p(布)")
randomNum = random.randint(0,len(storage)-1)
cpu = storage[randomNum]

if player == "s":
    print(f"你出{s}")
    print(f"電腦出{cpu}")
    if cpu == s:
        print("平手")
    elif cpu == r:
        print("你輸了")
    elif cpu == p:
        print("你贏了")
elif player == "r":
    print(f"你出{r}")
    print(f"電腦出{cpu}")
    if cpu == s:
        print("你贏了")
    elif cpu == r:
        print("平手")
    elif cpu == p:
        print("你輸了")

elif player == "p":
    print(f"你出{p}")
    print(f"電腦出{cpu}")
    if cpu == s:
        print("你輸了")
    elif cpu == r:
        print("你贏了")
    elif cpu == p:
        print("平手")

