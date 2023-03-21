# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: 20211207
# Date: 2022.03.05

retriever_count , exclude_count , progress_count , trailer_count = 0,0,0,0                           # count initialize to zero
while True:
    while True:
            try:
                 no_of_credits_at_pass = int(input("Enter your credits at pass: "))
                 no_of_credits_at_defer = int(input("Enter your credits at defer: "))
                 no_of_credits_at_fail = int(input("Enter your credits at fail: "))
                 if  (no_of_credits_at_pass % 20 == 0 and no_of_credits_at_defer % 20 == 0 and no_of_credits_at_fail % 20 == 0) and ( 0<= no_of_credits_at_pass <= 120 and 0<= no_of_credits_at_defer <= 120 and 0<= no_of_credits_at_fail <= 120):  
                     break
                 else:
                     print("Out of range")
            except ValueError:                                                    # check data type
                print("Integer required")
    while True:
              total = no_of_credits_at_pass + no_of_credits_at_defer + no_of_credits_at_fail            
              if total > 120 or total < 120:                                                                                
                  print("Total incorrect")
                  break
              elif 0 <= no_of_credits_at_pass <=80 and 0 <= no_of_credits_at_defer <=120 and 0<= no_of_credits_at_fail<=60: 
                  print("Do not progress - module retriever")
                  retriever_count +=1                                          # increase by 1 retriever count
                  break
              elif 0 <= no_of_credits_at_pass <= 40 and 0<= no_of_credits_at_defer <= 40 and 0 <= no_of_credits_at_fail <= 80:
                  print("Exclude")
                  exclude_count +=1                                           # increase by 1 exclude count
                  break
              elif no_of_credits_at_pass == 120 and no_of_credits_at_defer == 0 and no_of_credits_at_fail == 0:
                  print("progress")
                  progress_count +=1                                        # increase by 1 progress count
                  break
              elif no_of_credits_at_pass == 100 and 0 <= no_of_credits_at_defer <= 20 and 0<= no_of_credits_at_fail<= 20:
                  print("progress (module trailer)")
                  trailer_count +=1                                            # increase by 1 trailer count
                  break
    while True:
            print("Would you like to enter another set of data ? ")
            option = input("Enter 'y' for yes or 'q' to quit and view results : ")
            option = option.lower()                  
            if option == "y":                                                 # entering y if want to continue
                break
            elif option == "q":         # entering q if want to quit
                    print()
                    print("----Horizontal histogram----")                                                                # print horizontal histogram progress, trailer, retriever, exclude
                    print(f"progress {progress_count} :"   ,progress_count * "*")                  
                    print(f"trailer {trailer_count} :" ,trailer_count * "*")
                    print(f"retriever {retriever_count} :"  ,retriever_count * "*")
                    print(f"exclude {exclude_count} :"  ,exclude_count * "*")
                    print()
                    print(retriever_count + exclude_count + progress_count + trailer_count, "outcomes in total")
            else:
                    print("Wrong value")
            print("---------------------------------------------------------------")
            exit()
    
            
         
             
                  
             
            
         
         
         
         
        
        
        
    
