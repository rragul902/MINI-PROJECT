print("welcome to IPL Ticket Booking :)")
print("1.csk vs rcb")
print("2.mi vs kkr")
print("3.dc vs rajasthan royals")
SELECTMATCH=int(input("1/2/3:"))
STADIUM=input("cheppauk or chinnasamy stadium")
SEAT_CATEGORY=input("vip,regular,economy")
NUMBER_OF_SEATS=int(input("enter your seats"))

if SEAT_CATEGORY=="vip":
    price_per_seat=5000
elif SEAT_CATEGORY=="regular":
    price_per_seat=2500
elif SEAT_CATEGORY=="economy":
    price_per_seat=500        
TOTAL_AMOUNT=NUMBER_OF_SEATS*price_per_seat
if TOTAL_AMOUNT>10000:
    discount=TOTAL_AMOUNT*(25/100)
else:
    discount=0
final_price=TOTAL_AMOUNT-discount
#booking summary
print("/ bill summary")
if SELECTMATCH==1:
    print("MATCH: 1.csk vs rcb")
elif SELECTMATCH==2:
    print("MATCH:2.mi vs kkr")
elif SELECTMATCH ==3:
    print("MATCH:3.dc vs rajasthan royals")    
print("stadium:",STADIUM)
print("seat category:",SEAT_CATEGORY)    
print("TOTAL AMOUNT:",TOTAL_AMOUNT)
print("DISCOUNT APPLIED:",discount)
print("FINAL AMOUNT TO PAY:",final_price)

print("BOOKING CONFIRMED. THANK YOU !")
