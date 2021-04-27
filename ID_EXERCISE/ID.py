id_num = input("Please enter your ID: ")
id_year = id_num [:2]
print("Year: " + "19"+str(id_year))
id_month = int (id_num [2:4])
if id_month == 1:
    print("Month: " + "January")
elif id_month == 2:
    print("Month: "+ "February")
elif id_month == 3:
    print("Month: "+ "March")
elif id_month == 4:
    print("Month: "+ "April")
elif id_month == 5:
    print("Month: "+ "May")
elif id_month == 6:
    print("Month: "+ "June")
elif id_month == 7:
    print("Month: "+ "July")
elif id_month == 8:
    print("Month: "+ "August")
elif id_month == 9:
    print ("Month: "+ "September")
elif id_month == 10:
    print("Month: "+ "October")
elif id_month == 11:
    print("Month: "+"November")
elif id_month == 12:
    print("Month: "+ "December")
id_day = id_num [4:6]
print("Day: "+ str(id_day))
id_gender = id_num [6:10]
print("ID gender: " + id_gender)
print(type (id_gender))
gender_num = int (id_gender)
if gender_num >= 0000 and gender_num <= 4999:
    print("Gender: "+ "FEMALE!")
else:
    print("Gender: "+ "MALE!")
