import csv

testcase = []

with open('testcase.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        testcase.append(row)
    pass
pass

labels = testcase.pop(0)
print(labels)
print (testcase)

greedy = []
for case in testcase:
    if greedy is None:
        greedy = case
        pass
    else:
        isTrue = False
        nilai = 0
        while(isTrue == False and nilai < len(greedy)):
            if len(greedy[nilai][1]) < len(case[1]):
                isTrue = True
                greedy.insert(nilai,case)
                pass
            else:
                nilai += 1
            pass
        pass    
    if isTrue == False:
        greedy.append(case)
        pass
    pass 
pass
print (greedy)
