# import tabula
#
# table = tabula.read_pdf('weather.pdf', page=2)
# print(table)

# import camelot
#
# table = camelot.read_pdf('weather.pdf', page=2)
# print(table)

import camelot

# Read PDF into DataFrame
tables = camelot.read_pdf("file.pdf", pages='all')

# Print extracted tables
print(tables)
