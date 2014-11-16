# dtch.info
# Version: 0.01
# converts temperatures between celsius and farenheit
# http://dtch.info/code/temp.py

temp = int(input("Temperature: "))

conv = raw_input("Convert to Farenheit (f) or Celsius (c)?\n")

if conv == "c":
    print "Converting %d to celsius" % temp
    ctemp0 = temp - 32
    ctemp1 = ctemp0 / 5
    ctemp2 = ctemp1 / 9
    print "The new temp is %d" % ctemp2
elif conv == "f":
    print "Converting %d to farneheit" % temp
    ftemp0 = temp * 9
    ftemp1 = ftemp0 / 5
    ftemp2 = ftemp1 + 32
    print "The new temp is %d" %ftemp2
    
