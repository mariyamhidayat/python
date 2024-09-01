import qrcode
#UPI-ID format://pay?pa=UPI_ID&pn-Name&am-Amount&cu-Currency&tn=Message
UPI_ID=input("Enter your UPI ID:")
google_pay_url=f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'
google_pay_qr=qrcode.make(google_pay_url)
google_pay_qr.save('google_pay_qr.png')
google_pay_qr.show()
