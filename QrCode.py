import qrcode

website_url="https://www.joybagaccessory.com/"



qr = qrcode.QRCode(
    version=1,  # Boyut kontrolü (1 en küçük boyuttur)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
    box_size=10,  # QR kod kutusunun boyutu
    border=4,  # QR kodun etrafındaki kenarlık
)


qr.add_data(website_url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

# QR kodunu kaydet
img.save("website_qr_code.png")

print("QR kodu başarıyla oluşturuldu ve 'website_qr_code.png' olarak kaydedildi.")
