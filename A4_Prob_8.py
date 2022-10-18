# Write a python script to calculate simple interest.

Amount=float(input("Enter Principal Amount: Rs."))
Time=float(input("Enter Time in Years: "))
Roi=float(input("Enter ROI to calculate SI: "))
Simple_intrest= (Amount*Roi*Time)/100.0
print("Simple Intrest is: Rs.",Simple_intrest)
