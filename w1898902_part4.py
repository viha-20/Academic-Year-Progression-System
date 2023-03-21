# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: 20211207
# Date: 2022.04.01

retriever_count , exclude_count , progress_count , trailer_count = 0,0,0,0              # count initialize to zero
list_1 = []                                  # create thr list as a tempory list
while True:
    while True:
            try:
                 no_of_credits_at_pass = int(input("Enter your credits at pass: "))                                 # enter credit pass
                 if  no_of_credits_at_pass % 20 == 0 and 0 <= no_of_credits_at_pass <= 120:
                     break
                 else:   
                     print("Out of range")
            except ValueError :
                     print("integer required")                    # check  data type  
    while True:
                  try:
                    no_of_credits_at_defer = int(input("Enter your credits at defer: "))                           # enter credit defer
                    if  no_of_credits_at_defer % 20 == 0 and 0 <= no_of_credits_at_defer <= 120:
                        break
                    else:   
                        print("Out of range")
                  except ValueError :
                      print("integer required")
    while True:
                  try:
                    no_of_credits_at_fail = int(input("Enter your credits at fail: "))                                   # enter credit fail
                    if  no_of_credits_at_fail % 20 == 0 and 0 <= no_of_credits_at_fail <= 120:
                        break
                    else:   
                        print("Out of range")
                  except ValueError :
                      print("integer required")
    while True:
              total = no_of_credits_at_pass + no_of_credits_at_defer + no_of_credits_at_fail
              if total > 120 or total< 120:                                               # check total calculation for credits
                  print("Total incorrect")                                           
                  break
              elif 0 <= no_of_credits_at_pass <=80 and 0 <= no_of_credits_at_defer <=120 and 0<= no_of_credits_at_fail<=60:   # retriever outcome level
                  print("Do not progress - module retriever")                                                                                 # assign credits to variable retriever
                  retriever = f"{no_of_credits_at_pass},{no_of_credits_at_defer},{no_of_credits_at_fail}"
                  list_1.append("module retriever - ")
                  list_1.append(retriever)                                                            # retriever credits append to the list
                  retriever_count +=1                                                                  # retriever count increase by 1
                  break
              elif 0 <= no_of_credits_at_pass <= 40 and 0<= no_of_credits_at_defer <= 40 and 0 <= no_of_credits_at_fail <= 80:   # exclude outcome level
                  print("Exclude")
                  exclude = f"{no_of_credits_at_pass},{no_of_credits_at_defer},{no_of_credits_at_fail}"            # assign credits to variable exclude   
                  list_1.append("Exclude - ")                                                                                                   
                  list_1.append(exclude)                                                                                                           # exclude credits append to the list
                  exclude_count +=1                                                                                                                # exclude count increase by 1
                  break
              elif no_of_credits_at_pass == 120 and no_of_credits_at_defer == 0 and no_of_credits_at_fail == 0:        # progress outcome level
                  print("progress")
                  progress = f"{no_of_credits_at_pass},{no_of_credits_at_defer},{no_of_credits_at_fail}"         # assign credits to variable progress
                  list_1.append("progress -  ")
                  list_1.append(progress)                                                                                                        # progress credits append to the list
                  progress_count +=1                                                                                                              # progress count increase by 1
                  break
              elif no_of_credits_at_pass == 100 and 0 <= no_of_credits_at_defer <= 20 and 0<= no_of_credits_at_fail<= 20:    # trailer outcome level
                  print("progress (module trailer)")
                  trailer = f"{no_of_credits_at_pass},{no_of_credits_at_defer},{no_of_credits_at_fail}"                #assign credits to variable trailer
                  list_1.append("progress(module trailer)  - ")
                  list_1.append(trailer)                                                                                             # trailer credits append to the list
                  trailer_count +=1                                                                                                   # trailer count increase by 1
                  break
    while True:
            print("Would you like to enter another set of data ? ")
            option = input("Enter 'y' for yes or 'q' to quit and view results : ")
            option = option.lower()
            if option == "y":                          # enter y if want to continue
                break
            elif option == "q":       # enter q if want to quit
                    print()
                    print("----Horizontal histogram----")                                                                # print horizontal histogram progress, trailer, retriever, exclude
                    print(f"progress {progress_count} :"   ,progress_count * "*")                  
                    print(f"trailer {trailer_count} :" ,trailer_count * "*")
                    print(f"retriever {retriever_count} :"  ,retriever_count * "*")
                    print(f"exclude {exclude_count} :"  ,exclude_count * "*")
                    
                    print()
                    print("----Vertical Histogram----")
                    credit_name = ['progress','trailer','retriever','exclude']                             # create list outcome for vertical histogram
                    print(credit_name[0],credit_name[1],credit_name[2],credit_name[3])           #  print outcomes using indexing
                    for x in range(max(progress_count,trailer_count,retriever_count,exclude_count)):
                        print("  {0}            {1}           {2}           {3}".format(                                                       # vartical histogram credits star outcomes printing
                                 '*' if x < progress_count else '  ',
                                 '*' if x < trailer_count else '   ',
                                 '*' if x < retriever_count else '   ',
                                 '*' if x < exclude_count else '  '))
                    print()
                    print(retriever_count + exclude_count + progress_count + trailer_count, "outcomes in total")
                    print()
            else:
                    print("Wrong value You should enter 'y' or 'q'")
                    break
            print(list_1)                                                  # print temp list with whole outcomes and credits
            for i in range (0,len(list_1),2) :                    # breaking from large tempory list to small lists
                credit = list_1[i] + list_1[i+1]
                print(credit)                                           # printing each outcomes  and  each credits line by line
            f = open("credit.txt","w")                      # create text file named 'credit' to write
            for i in range (0,len(list_1),2) :
                credit = list_1[i] + list_1[i+1]
                f.write(credit)                                # write in list credit to the text file 
                f.write("\n")                                  # write outcomes to the text file line by line
            f.close()
            f = open("credit.txt","r")                        # open the text file named 'credit' for read
            for i in range (0,len(list_1),2) :
                credit = list_1[i] + list_1[i+1]
                f.readline( )    # read outcomes in text file
            f.close()                                              
            exit()
                                   
            
        
            
