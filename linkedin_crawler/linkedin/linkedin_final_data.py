import csv

f = open('whole_data.txt', 'r')

fields = ['email']

email_dict = []

for data in f.readlines():

    if '@' in data:

        print data

        email_dict.append({
            'email' : data.lstrip().rstrip()
        })


with open('linkedin_final_data.csv', 'w') as csvfile: 
    # creating a csv writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields)
      
    # writing the header 
    writer.writeheader()
        
    writer.writerows(email_dict)