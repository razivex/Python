import pyotp

secret = "JBSWY3DPEHPK3PXP"

totp = pyotp.TOTP(secret)
print("Current OTP:", totp.now())
