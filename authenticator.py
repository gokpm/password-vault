import asyncio
import qrcode
import hmac, base64, struct, hashlib, time

def get_hotp(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

async def get_totp(secret):
    global otp
    flag = False
    while not flag:
        otp = get_hotp(secret, intervals_no=int(time.time())//30)
        await asyncio.sleep(0.0001)
        flag = match_flag
    return
        
def get_qr(username, key):
    qr = qrcode.QRCode(version=40,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=4,
                       border=4)

    qr.add_data('otpauth://totp/Vault:{0}?secret={1}&issuer=Vault'.format(username, key))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    return

async def input_otp():
    global match_flag
    i = 1
    while i < 4:
        otp_flag = False
        match_flag = False
        user_otp = input('Attempt {0} OTP: '.format(i))
        await asyncio.sleep(0.0001)
        if int(user_otp) == int(otp):
            otp_flag = True
            match_flag = True
            break
        else:
            print('ACCESS DENIED')
            i += 1
    if i > 3:
        match_flag = True
        print('ATTEMPTS EXCEEDED')
    return otp_flag
            



