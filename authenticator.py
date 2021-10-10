import hmac, base64, struct, hashlib, time
import qrcode

def get_hotp(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp(secret):
    return get_hotp(secret, intervals_no=int(time.time())//30)

def get_qr(username, key):
    qr = qrcode.QRCode(version=40,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=4,
                       border=4)

    qr.add_data('otpauth://totp/{0}?secret={1}'.format(username, key))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    return




