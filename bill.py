company = "vermaclabs"
address = "Madhapur, hyderabad"
date = "12/02/2019"
time = "11:49"
staff = "Deelip"

print("vermaclabs")
print("Madhapur, hyderabad")
print("date: 12/02/2019 11:49")
print("Saff: Deelip")

item = ("chinthal soap" , "colagate past" , "axe bodysprey" , "head&shoulders")
Qty = (3,2,2,1)
price = (105,100,199,45)

print("Vermaclabs".center(30))
print("Madhapur, hyderabad".center(30))
print("date : 12/02/2019  Time: 11:49".center(40))
print("staff    deelip".center(30))
print("_"*30)
a,b,c,d = 3,2,2,1
w,x,y,z = 105,100,199,45
print(" 1 " + " chinthal soap " + " {}     {}".format(str(a),a*w))
print(" 2 " + " colagate past " + " {}     {}".format(str(b),b*x))
print(" 3 " + " axe bodysprey " + " {}     {}".format(str(c),c*y))
print(" 4 " + " head$shoulders " + "{}     {}".format(str(d),d*z))
n = (a*w) + (b*x) + (c*y) + (d*z)
GST = n*0.03
total = n + GST
print("sub total".center(23),n)
print("_"*30)
print("TOTAL".center(23),n)
