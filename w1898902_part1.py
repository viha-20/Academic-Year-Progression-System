# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: 20211207
# Date: 2022.03.05

# Part 1 - Main Version
#1)
i = 0
while i < 1:
    while True :
        try:
            no_of_credits_at_pass = int(input("Enter your credits at pass : "))    # enter pass credits
            if no_of_credits_at_pass % 20 == 0 and 0 <= no_of_credits_at_pass <= 120 :
                break
            else:
                print("Out of Range")                           # if credit not in range
        except ValueError:
            print("Integer Required")                           # error handle
        
    while True:
        try:
            no_of_credits_at_defer = int(input("Enter your credits at defer : "))    # enter defer credits
            if no_of_credits_at_defer % 20 == 0 and 0 <= no_of_credits_at_defer <= 120 :
                break
            else:
                print("Out of Range")                   # if credit not in range
        except ValueError:
            print("Integer Required")                 # error handle
        
    while True:
        try:
            no_of_credits_at_fail = int(input("Enter your credits at fail : "))    # enter defer credits
            if no_of_credits_at_fail % 20 == 0 and 0 <= no_of_credits_at_fail <= 120 :
                break
            else:
                print("Out of Range")                 # if credit not in range
        except ValueError:
            print("Integer Required")          # error handle
         
    while i< 1:
        total = no_of_credits_at_pass + no_of_credits_at_defer + no_of_credits_at_fail
        if total > 120 or total < 120 :
            print("Total incorrect")
            break
        elif 0 <= no_of_credits_at_pass >= 40 and 0<= no_of_credits_at_defer <= 40 and no_of_credits_at_fail >= 80:                       # exclude outcome level
            print("Exclude")
            break
        elif 0 <= no_of_credits_at_pass <=80 and 0 <= no_of_credits_at_defer <=120 and 0<= no_of_credits_at_fail<=60:           # retriever outcome level
            print("Do not progress - module retriever")
            break
        elif no_of_credits_at_pass == 120 and no_of_credits_at_defer == 0 and no_of_credits_at_fail == 0:                                     # progress outcome level
            print("Progress")
            break
        elif no_of_credits_at_pass == 100 and 0 <= no_of_credits_at_defer <= 20 and 0<= no_of_credits_at_fail<= 20:              # module trailer outcome level
            print("Progress (module trailer)")
            break
        else:
            print()
            break
    i+=1
i+=1


    
        
    
        
        
    
    
    
    
