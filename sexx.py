import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import sexx64_
elif bit == '32bit':
    import sexx32_
