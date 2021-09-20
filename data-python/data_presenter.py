data = open('./CupcakeInvoices.csv')

for row in data:
  print(row)

data = open('./CupcakeInvoices.csv')
for row in data:
  inputs = row.split(',')
  print(inputs[2])

data = open('./CupcakeInvoices.csv')
for row in data:
  inputs = row.split(',')
  final = int(inputs[3]) * float(inputs[4])
  print(final)

final = 0
data = open('./CupcakeInvoices.csv')
for row in data:
  inputs = row.split(',')
  final = final + (int(inputs[3]) * float(inputs[4]))
print(final)


