Customer = raw_input("Enter a name for Customer")
Bill = input("enter a value")
Discount = input("enter a percentage of a value")
Cashier = raw_input("enter a name for Cashier")
Total = 0
Total = (Bill-((Bill*Discount)/100.0))
print"output:"  
print"-------------------"
print"INVOICCE"
print"-------------------"
print"Customer:",Customer
print"Bill Amount:","RS",Bill  
print"Discount:",Discount,"%"
print"Total:","Rs",Total
print"--------------------"
print"Cashier:",Cashier
print"--------------------"
