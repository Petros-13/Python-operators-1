print("Welcome to World bank")
name=input("Enter your name:")
print("Welcome",name,"to world bank")
print("Enter the ammount you would like to withdraw")
ammount=int(input("Enter the ammount:"))
note500=ammount//500
note100=(ammount%500)//100
note50=((ammount%500)%100)//50
note10=(((ammount%500)%100)%50)//10
note5=((((ammount%500)%100)%50)%10)//5
print("The ammount of 500 dollar bills you withdrawed are",note500)
print("The ammount of 100 dollar bills you withdrawed are",note100)
print("The ammount of 50 dollar bills you withdrawed are",note50)
print("The ammount of 10 dollar bills you withdrawed are",note10)
print("The ammount of 5 dollar bills you withdrawed are",note5)