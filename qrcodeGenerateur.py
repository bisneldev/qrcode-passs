from json import dumps
import qrcode
import cbor2
import zlib
import base45


#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=4,
        border=5
)

donnees = {
    'organisme_emetteur': "JAYGM",
    'name' :"jay",
    'prename' : "sibang",
    'birth_date' : "05/07/1998",
    'type_de_pass': "collecteur jay",
}

#encodage en CBOR
data = donnees.copy()

data_en_cbor = cbor2.dumps(data)

#compression en zlib
data_en_zlib = zlib.compress(data_en_cbor)

#encodage en base45
data_en_base45 = base45.b45encode(data_en_zlib)

#rajout du préfixe HC1:
data_final = "HC1:".join(str(data_en_base45))



qr.add_data(donnees)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('passjayGM.png')

