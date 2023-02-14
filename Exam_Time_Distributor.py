import time

def TimeDistributor():
    """
    Takes two inputs: total exam time and total number of questions. Returns time per question.
    Prompts user for input at the start of the exam. Each input marks a complete question.
    Returns new time per question and remaining time/number of questions.
    """
    tot_time = int(input("Enter the total exam time in seconds: ")) 
    num_of_q = int(input("Enter the total number of questions: "))
    time_per_q = round((tot_time / num_of_q), 3)
    if time_per_q < 60:         #checks if time is more than 1 minute (60 seconds).
        print("Time per question for this exam is:",time_per_q,"seconds.")
    else:
        time_per_q_minute = time_per_q//60
        time_per_q_seconds = round(((time_per_q/60 - time_per_q//60) * 60), 3)
        print("Time per question is:",time_per_q_minute,"minutes and",time_per_q_seconds,"seconds.")  #output in minutes and seconds.
        
    print("Press ENTER to count laps.\nPress SPACEBAR to stop") #defines user interaction, each ENTER input marks new question.
    try:
        while True:
            
            starttime=time.time() 
            lasttime=starttime #allows "lapping" times, i.e. real time spent per question
            q_number=1
        
            input()
            q_time=round((time.time() - lasttime), 2)
            totaltime_exam = round((time.time() - starttime), 2)
            print("*"*10)
            print("Time spent on Question: "+str(q_time),"seconds.")
            print("-"*10)
            lasttime=time.time()
            
            q_number+=1
            num_of_q+=-1
            print("Remaining questions:", num_of_q)
            tot_time = round((tot_time - q_time), 3)
            print("Remaining total time:", tot_time, "seconds.")
            time_per_q = round((tot_time / num_of_q),3)
            print("-"*10)
            print("New time per question:", time_per_q,  "seconds.") #main output, describes new time per question.
            print("-"*10)
            print("*"*10)
            
    except KeyboardInterrupt:
        print("Done")

TimeDistributor() #calls the function.
