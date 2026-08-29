import random
num=random.randint(100000,999999)
print("-----------------OTP verification---------------")
print("We send an otp to your mobile")
print("OTP IS: ")
print(num)
Input=int(input("Enter your OTP here: "))
if Input==num:
    print("OTP is correct")
else:
    print("OTP is Invalid Please try again")
