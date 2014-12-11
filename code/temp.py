# dtch.info
# Current Version: 0.06
# converts temperatures between celsius and farenheit
# http://dtch.info/code/temp.py
# Changelog:
# 0.06  - switched from int to float for more precise
#       measurements
# 0.05  - %s/far*/farenheit
# 0.04  - simplified code (thanks to pulse on ##programming)
# 0.03  - fixed issue #001: temperatures converting to celsius coming out wrong
# 0.02  - print statements changed
# 0.01  - Initial Code

temp = float(input("Temperature: "))

conv = raw_input("Convert to Farenheit (f) or Celsius (c)?\n")

if conv == "c":
    print "Converting %d farenheit to celsius" % temp
    ctemp = (temp - 32.0) / 1.8
    print "The new temp is %d celsius" % ctemp
elif conv == "f":
    print "Converting %d celsius to farenheit" % temp
    ftemp = (temp * 1.8) + 32.0
    print "The new temp is %d farenheit" % ftemp 
