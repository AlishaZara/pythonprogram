import csv
# with open('mca.csv','w',newline='')as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id', 'name', 'mobile','email'])
#     data2=[
#         [1,'John',9090909090,'johnexample.com' ],
#         [2,'alex',9090909092,'alexexample.com'],
#         [3,'rolex',909090993,'rolexexample.com'],
#     ]
#     data.writerows(data2)

# with open ('mca.csv','r')as csvfile:
#     data= csv.reader(csvfile)
#     for i in data:
#         print(i)

with open ('mca1.csv','w')as csvfile:
    fieldnames=['id', 'name', 'mobile','email']
    data=csv.DictWriter(csvfile,fieldnames)
    data.writeheader()
    rows=[
        {'id':1,'name':'lijitha','mobile':9090909090,'email':'l@gmail.com'},
        {'id':2,'name':'gurushiva','mobile':9090909099,'email':'g@gmail.com'},
    ]
    data.writerows(rows)

with open ('mca1.csv','r')as csvfile:

    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])
        print(row)