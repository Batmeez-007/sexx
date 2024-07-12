import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import sexx64_enc
elif bit == '32bit':
    import sexx32enc_
