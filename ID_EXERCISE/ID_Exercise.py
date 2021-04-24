id_num = str(input("Please enter your ID number: ")) #The user ID is entered
id_length_num = len(id_num) # The length of the ID is sought for

if id_length_num == 13: #If the length is 13 digits, the code continues
    south_african = id_num[10] # The 10th digit is sought for
    if south_african == "0": #If the 10th digit is 0, the person is an S.A citizen
        print("SA CITIZEN!")
    elif south_african == "1": #If the 10th digit is 1, the person is a permanent resident
            print("PERMANENT S.A CITIZEN!")
    elif south_african != 0 or south_african != 1: #If neither 0 nor 1, they are not a citizen
        print("NOT AN S.A CITIZEN!")
else:
    print("Out of range!") #If the length is less than 13 or greater, this is not an ID number

