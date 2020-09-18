#######################################################################################
# This proyect lists prime numbers and print a total of prime numbers in a range
# And calculate the Time elapsed of the job
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################


from datetime import datetime
start_time = datetime.now()

# Prime number checking function
def IsPrime(num):
    for i in range(3, int((num**0.5))+1, 2):
        if num % i == 0:
            return False
    return True

# Listing prime numbers and counting total prime numbers function
def list_prime(limit):
    count = 1 #limit is greater than 1
    print('2 is a prime number')
    for j in range(3, limit+1, 2):
        if IsPrime(j):
            count += 1
            print(f'{j} is a prime number')
    print(f'In range 1 - {limit} are {count} total prime numbers')


# Main
max = 10000 #This var must be greater than 1
list_prime(max)
print()
time_elapsed = datetime.now() - start_time
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
