import glob


files = glob.glob('clients/14I/*.{}'.format('R4I'))

email_addresses = []

for file in files:
    data = ""
    with open(file, encoding='utf-8', errors='ignore') as f:
        data = f.read()

    try:
        pos1 = data.index('.55') + 5
    except:
        pos1 = 999

    try:
        pos2 = data.index('.56') + 5
    except:
        pos2 = 999

    this_email = ""
    counter = 0
    keep_going = True
    if pos1 == 999:
        keep_going = False
    while keep_going:
        this_email += data[pos1]
        pos1 += 1
        counter += 1
        if counter > 4:
            finished = this_email[-4:]
            if finished == '.com' or finished == '.net' or finished == '.gov' or finished == '.edu':
                keep_going = False
                email_addresses.append(this_email)
        if counter > 150:
            keep_going = False

    this_email = ""
    counter = 0
    keep_going = True
    if pos2 == 999:
        keep_going = False
    while keep_going:
        this_email += data[pos2]
        pos2 += 1
        counter += 1
        if counter > 4:
            finished = this_email[-4:]
            if finished == '.com' or finished == '.net' or finished == '.gov' or finished == '.edu':
                keep_going = False
                email_addresses.append(this_email)
        if counter > 150:
            keep_going = False

print(email_addresses, len(email_addresses))



# .40  Charles \*18,16,S,25
# .42  Ainsworth \*18,49,S,25
# .45  Miriam \*19,16,S,25
# .47  Ainsworth \*19,49,S,25
# .55  scotty.birdsell@gmail.com \*35,31,S,31
# .56  rotorgrl60@yahoo.com \*35,65,S,31
