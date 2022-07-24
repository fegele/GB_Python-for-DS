from collections import OrderedDict

attributes = ('name', 'quarter_1_profit', 'quarter_2_profit', 'quarter_3_profit', 'quarter_4_profit')
n = int(input("Enter number of companies : "))

companies = []
for i in range(0, n):
    company = OrderedDict()
    for key in attributes:
        company[key] = input(f"Enter company's {key} : ")
    company['annual_profit'] = sum([int(company[key]) for index, key in enumerate(company) if index > 0])
    companies.append(company)

average_profit = sum([c['annual_profit'] for c in companies]) / len(companies)
print(f'Average annual profit: {average_profit}')

print(f'Companies with profits below average:')
for c in companies:
    if c['annual_profit'] < average_profit:
        print(c['name'])
print(f'Companies with profits above or equal to average:')
for c in companies:
    if c['annual_profit'] >= average_profit:
        print(c['name'])
