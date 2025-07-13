table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):
    colWidths = [0] * len(table_data)

    for i, col in enumerate(table_data):
        colWidths[i] = max(len(item) for item in col)
    num_rows = len(table_data[0])

    for row in range(num_rows):
        line = ''
        for col in range(len(table_data)):
            line += table_data[col][row].rjust(colWidths[col]) + ' '
        print(line)

print_table(table_data)
