import csv
with open('mca.csv','w',newline='')as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id', 'name', 'mobile','email'])
    data2=[
        [1,'John',9090909090,'johnexample.com' ],
        [2,'alex',9090909092,'alexexample.com'],
        [3,'rolex',909090993,'rolexexample.com'],
    ]
    data.writerows(data2)