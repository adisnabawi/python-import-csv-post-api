import requests
from csv import reader
with open('Data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        for row in csv_reader:
            if "ID" not in row[0]:
                url = 'YOUR API'

                try:
                    myobj = {
                                "access_key": "YOUR ACCESS TOKEN",
                                "power": row[3],
                                "energy": row[4],
                                "devicetime": row[2]
                            }
                    x = requests.post(url, data = myobj)
                    print(myobj)
                except IndexError:
                    pass