units = input ("Number of units consumed:")
if units<=50:
    total_bill = (units * 5)
elif units<=150:
    total_bill = (50*5)+((units-50)*7)
elif units>150: 
    total_bill = ((50*5)+(100*7)+((units-150)*10))
    print "Total Bill:","Rs.",total_bill+(total_bill*0.2)
