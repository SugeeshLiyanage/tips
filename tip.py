def total(bill_amount,tip):
    total = bill_amount*(1+0.1*tip)
    total = round(total,2)
    print ("please pay${total}")
total(150,20)