class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        pass

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        pass

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def parse_data(data):
    row_split = '-----'
    data_row = data.split(row_split)
    result = []
    bank_price, entry_price ,close_price = 0,0,0
    for row_index in data_row:
        bank_i = row_index.find('BANK:')
        entry_i = row_index.find('Entry:')
        target_i = row_index.find('Target:')
        close_i = row_index.find('Close:')
        
    pass


def main():


# content = read_data('deals.txt')
# result = content
# write_data('out.txt', result)


if __name__ == '__main__':
    main()
