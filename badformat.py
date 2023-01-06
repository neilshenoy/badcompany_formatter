
import csv

originalcsv_location = input(str('Enter full path of original csv file: '))
finalcsv_name = input(str('Enter name of new csv file: '))

with open(originalcsv_location, 'r') as originalcsv:
    csv_reader = csv.DictReader(originalcsv)

    with open(finalcsv_name, 'w') as finalcsvtest:

        fieldnames = ['Name', 'Seat', 'Date']

        csv_writer = csv.DictWriter(finalcsvtest, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_reader:
            try:
                fieldlist = line[None]
            except:
                continue

            try:
                firstname = fieldlist[0]
                lastname = fieldlist[1]
                eventdate = fieldlist[3]
                tickettype = fieldlist[4]
                seatinfo = fieldlist[7]
                ticketquantity = fieldlist[9]
            except:
                continue
            fullname = firstname + ' ' + lastname
            eventdate = eventdate.split(':')
            try:
                ampm = eventdate.pop(2)
                ampm = ampm.split(' ')
                finaldate = eventdate[0] + ':' + eventdate[1] + ' ' + ampm[1]
            except:
                continue
            seatinfo = seatinfo.split(' - ')
            try:
                finalinfo = seatinfo[2] + ' ' + seatinfo[3]
            except:
                continue
            if tickettype == 'SubFree':
                finalinfo = finalinfo + ' [S]'
            if int(ticketquantity) == 0:
                continue
            elif int(ticketquantity) == 1:
                csv_writer.writerow({'Name':fullname, 'Seat':finalinfo, 'Date':finaldate})
            else:
                print(ticketquantity + ' is being treated as 1.')
                csv_writer.writerow({'Name': fullname, 'Seat': finalinfo, 'Date': finaldate})
