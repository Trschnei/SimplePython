#Travis Schneider - CS 161 HW2
#The purpose of my program is to calculate the cost of electricity to run an indoor garden


print ("Halligan's Indoor Garden Tent Cost Calculator")
print ("All of your answers should be in number only form, we know the units")
lightWatts= int(input ("What wattage HID light are you using?"))
#setup if then statement to have 400, 600, 1000 watts equal their kilowatt equivilent
if lightWatts == 400:
    ballastWatts =.4
elif lightWatts == 600:
    ballastWatts =.6
elif lightWatts == 1000:
    ballastWatts = 1
else:
    print ("Error I do not understand, Goodbye")

timeWatts= float(input ("How many hours per day will the light be on?"))

fan= int(input("Are you using a 4, 6, or 8 inch inline fan?"))
#setup and if then statement so that the size is equal to a kilowatts
if fan == 4:
    fanWatts = .090
elif fan == 6:
    fanWatts= .135
elif fan == 8:
    fanWatts = .164
else:
    print ("Error I do not understand, Goodbye")
    
print ("It is recommended that you run your fan 24 hours a day , but..")
fanTime= float(input ("How many hours per day are you running your fan?"))

circulation= float(input ("How many small oscillating fans are you using?"))
#needs an equation for number of fans times the wattage for a single fan a oscillating fan take approx 100watt or .1kw for 24 hours
circulationFan= circulation * .01



#forumla to calculate total cost per month and per year
#separate and calculate on separate lines
totalLight= ballastWatts* timeWatts
totalFan= fanWatts* fanTime
totalWatts= totalLight + totalFan + circulationFan
costPerHour= .12 #cents per kilowatt
dailyCost= totalWatts*costPerHour
monthlyCost= dailyCost*30
yearlyCost= monthlyCost*12
print ("your approximate daily cost is:", dailyCost)
print ("your approximate monthly cost is:", monthlyCost)
print ("your approximate yearly cost is:", yearlyCost)
input ("")
