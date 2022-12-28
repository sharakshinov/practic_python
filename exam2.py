class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        return self.targets

    def get_target_percents(self, target):
        return (target / self.entry - 1) * 100

    def get_target_banks(self, target):
        return self.bank * target / self.entry


def read_data(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def parse_data(data, split_symbol='-----'):
    bank = None
    entry = None
    close = None
    targets =[]
    gg = 0
    deals_data = data.split(split_symbol)
    deals = []
    for row in data:
        if row.startswith('Bank:'):
            first_index = row.find('Bank:')
            second_index = row.find('USD')
            bank = float(row[first_index + len('Bank: '): second_index])
            gg = bank
        elif row.startswith('Entry:'):
            first_index = row.find('Entry: ')
            second_index = row.find('USD')
            entry = float(row[first_index + len('Entry: '): second_index])

        elif row.startswith('Target: '):
            roww_splitt = row.split()
            for tt in roww_splitt[1:]:
                if tt.endswith("USD;"):
                    targets.append(float(tt[0:-4]))
                if tt.endswith("USD"):
                    targets.append(float(tt[0:-3]))

        elif row.startswith('Close: '):
            first_index = row.find('Close: ')
            second_index = row.find('USD')
            close = float(row[first_index + len('Close: '): second_index])

        deals.append(StrategyDeal(bank=bank, entry=entry, targets=targets, close=close))
    return deals


def main():
    content = read_data('deal.txt')
    print(parse_data(content))

# write_data('out.txt', result)


if __name__ == '__main__':
    main()
