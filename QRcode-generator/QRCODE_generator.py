
import qrcode


data = input("Enter a TEXT or URL: ").strip()

filename = input("Enter file name: ").strip().upper()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white' )
image.save(filename)

print(f'QR CODE saved as! {filename}')