import glob


files = glob.glob('Data/*/*.{}'.format('XX15'))

email_addresses = []

for file in files:
    data = ""
    keep_going = True
    with open(file, encoding='utf-8', errors='ignore') as f:
        data = f.read()
    print("##################", len(data))
    if 'Email' in data:
        skip = 0
        how_many = data.count('Email')
        print(how_many, "HOW  MANY")
        for each in range(how_many):
            this_email = ""
            pos = data.index('Email', skip)
            skip = pos + 5
            print(skip)
            letter_place = pos + 11
            print(letter_place)
            counter = 1
            keep_going = True
            while keep_going:
                this_email += data[letter_place]
                letter_place += 2
                counter += 1
                # print(letter_place, counter, keep_going, email_addresses)
                if counter > 4:
                    finished = this_email[-4:]
                    if finished == '.com' or finished == '.net' or finished == '.gov' or finished == '.edu':
                        keep_going = False
                        print("****************", email_addresses, each, "*****************")
                        email_addresses.append(this_email)
                if counter > 150:
                    keep_going = False
print(email_addresses, len(email_addresses))

#Email\x08\x00.\x00\x00\x00j\x00k\x00i\x00l\x00p\x00a\x00t\x00r\x00i\x00c\x00k\x00m\x00d\x00@\x00n\x00c\x00.\x00r\x00r\x00.\x00c\x00o\x00m
