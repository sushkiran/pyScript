"""
1.Read file bank-data.csv
2.Build a set of unique jobs
3.Read the input from command line –profession
4.Check if profession is in list
5.Print whether client is eligible

Further Enhancements
1.Compute max and min age for loan eligibility based on data in csv file
2.Store max and min age in dictionary
3.Make the profession check case insensitive
4.Currently program ends after the check.
Take the input in while loop and end only if user types "END" for profession
"""

import csv

age_set = set()
job_set = set()
with open('bank-data.csv') as file:
    reader = csv.reader(file)
    head_row = next(reader)
    for data_row in reader:
        age_set.add(int(data_row[0]))
        job_set.add(data_row[1])

age_dict = {
    'max': max(age_set),
    'min': min(age_set)
}
print(job_set)
print(age_dict)

profession = ''
while profession != 'END':
    profession = input('Enter your profession: ')
    text = 'Loan Eligibility {} for ' + profession
    if profession.lower() in job_set:
        print(text.format('APPROVED'))
    else:
        print(text.format('REJECTED'))
