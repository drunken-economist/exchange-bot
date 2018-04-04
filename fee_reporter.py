import csv

def fee_generator(filename):
    fees = {}
    print('opening '+filename)
    with open(filename, 'rb') as feefile:
        fee_reader = csv.reader(feefile, delimiter=';')
        for row in fee_reader:
            exchange_name = row[0]
            exchange_fee = row[1]
            exchange_comment = row[2]
            fees[exchange_name] = {
                'name': exchange_name,
                'fee': exchange_fee,
                'comment': exchange_comment
                }
        print(fees)
        return fees

def get_info(exchange_name, filename):
    fees = fee_generator(filename)
    print(fees)
    return fees[exchange_name]
