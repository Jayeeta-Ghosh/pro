
class atm:
    def_init_(self,name,age,gender,occupation,cash):
        self.name=name
        self.age=age
        self.gender=gender
        self.occupation=occupation
        self.cash=cash

    def input:
        a=input("Enter your name")
        b=input(int("enter your age"))
        c=input("enter your gender")
        d=input("input your occupation") 
        e=input(int("enter your cash"))

    def withdrawal:
        print("cash withdraw")

    def balanceEnquiry:
        print(e,"cash ")       

jayeeta=atm("jayeeta",,14,"female","student",1000)
rishit=atm("rishit",14,"male","student",1000)

jayeeta.input()
jayeeta.withdrawal()
jayeeta.balanceEnquiry()
rishit.input()
rishit.withdrawal()
rishit.balanceEnquiry()
