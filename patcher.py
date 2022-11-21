with open('Cyberpunk2077.exe','rb+') as f:
    f_contents = f.read()
    f.seek(0)
    search = b'\x75\x30\x33\xc9\xb8\x01\x00\x00\x00\x0f\xa2\x8b\xc8\xc1\xf9\x08'
    if search in f_contents:
        print("Unpatched file detected\nWould you like to patch it? (y/n):")
        input = str(input())

        if input == "y":
            f.seek(f_contents.index(b'\x75\x30\x33\xc9\xb8\x01\x00\x00\x00\x0f\xa2\x8b\xc8\xc1\xf9\x08'))
            f.write(b'\xeb')
            print("Executable has been successfully patched\nExiting...")
        elif input == 'n':
            print("exiting...")
        else:
            print("Invalid input exiting...")
    else:
        print("File has been patched\nWould you like to revert back? (y/n):")
        input = str(input())
        if input == "y":
                f.seek(f_contents.index(b'\xeb\x30\x33\xc9\xb8\x01\x00\x00\x00\x0f\xa2\x8b\xc8\xc1\xf9\x08'))
                f.write(b'\x75')
                print("Executable has been successfully reverted\nExiting...")
        elif input == 'n':
            print("exiting...")
        else:
            print("Invalid input exiting...")
