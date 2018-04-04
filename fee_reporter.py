import csv


def fee_generator(filename):
    fees = {}
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
        return fees
print(fee_generator('exchange_fee_schedule.txt'))
