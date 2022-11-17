#student name: Kevin Peng
#student number: 94742293

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, availableChopsticks: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        # while True loop so that philosopher will continue to check if they can acquire both chopsticks
        # when they are successful in acquiring both chopsticks and eating, the loop is broken.
        # otherwise, they continue to check if both chopsticks are available by (non-blocking) acquiring left and right availableChopsticks
        while True:
            # non-blocking acquire on available chopsticks
            canAcquireLeft = availableChopsticks[leftChopstick].acquire(block=False)
            canAcquireRight = availableChopsticks[rightChopstick].acquire(block=False)

            # if both locks were able to be acquired, then actually acquire the chopsticks
            if(canAcquireLeft and canAcquireRight): 
                #to simplify, try statement not used here
                chopstick[leftChopstick].acquire()
                print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
                chopstick[rightChopstick].acquire()
                print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

                eatForAWhile()  #use this line as is

                print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
                chopstick[rightChopstick].release()
                # release lock because chopstick is now available
                availableChopsticks[rightChopstick].release()
                print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
                chopstick[leftChopstick].release()
                # release lock because chopstick is now available
                availableChopsticks[leftChopstick].release()

                thinkForAWhile()  #use this line as is

                # break out of "while True" loop as philosopher managed to eat and think
                break
            else:
                # philosopher was unable to eat this iteration of the "while True" loop, so
                # release the availableChopsticks locks if they were acquired previously and repeat the loop
                if(canAcquireLeft):
                    availableChopsticks[leftChopstick].release()
                if(canAcquireRight):
                    availableChopsticks[rightChopstick].release()


if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstic
    numberOfPhilosophers = 5

    # list of locks for each chopstick
    # acquire calls should be non-blocking to check for if both chopsticks can be acquired
    # if both chopsticks can be acquired, then acquire semaphoreList chopstick
    lockList = list()

    """
    Note:

    The reason I am using a list of locks to represent available chopsticks rather than 
    directly calling non-blocking acquires on the original semaphoreList is because the 
    lab specification specifically says "allow a philosopher to pick up her chopsticks only if both chopsticks are available".

    If non-blocking acquires on the locks both return true, then both chopsticks are available to be acquired.
    """
   
    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick
        # one lock per available chopstick
        lockList.append(multiprocessing.Lock())

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, lockList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()