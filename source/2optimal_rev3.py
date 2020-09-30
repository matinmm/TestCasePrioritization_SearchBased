import csv
import json
import os

namafile = input("Input Nama File : ")

def searchJumlahFault(namafile):
    jumlahfault = 0
    for case in testcase:
        for num in case["Fault"]:
            if num > jumlahfault:
                jumlahfault = num
                pass
            pass
        pass
    return jumlahfault

def greedyAlgorithm(testcase) :
    greedy = []
    for case in testcase:
        if greedy is None:
            greedy = case
            pass
        else:
            isTrue = False
            nilai = 0
            while(isTrue == False and nilai < len(greedy)):
                if len(greedy[nilai]["Fault"]) < len(case["Fault"]):
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
    return greedy

def calculateAPFD(testcase,jumlahfault) :
    tfm = 0
    for i in range(jumlahfault):
        isFound = False
        nilai = 0
        while(isFound == False) :
            isFault = i+1
            isFound = isFault in testcase[nilai]["Fault"]
            if(isFound == True) :
                tfm += nilai+1
                pass
            nilai += 1
            pass
        pass
    #print(tfm)
    #print((tfm/(jumlahfault*len(testcase))+(1/(2*len(testcase)))))
    apfd = 1 - (tfm/(jumlahfault*len(testcase))+(1/(2*len(testcase))))   
    return apfd
try:
    f = open(f'{namafile}.json', "r")
    testcase = json.loads(f.read())
    jumlahfault = searchJumlahFault(testcase)
except IOError:
    print("Nama file yang diinputkan Salah")
    os._exit(1)
    


temp = []
kombinasi = []
gabungan = set(kombinasi)
testcase = greedyAlgorithm(testcase)
optimal = testcase.copy()

count = 0


while(len(gabungan) != jumlahfault):
    for case in testcase:
        hold = testcase.index(case)
        nilai = testcase.index(case) + 1
        while (nilai < len(testcase)):
            faulthold = set(testcase[hold]["Fault"])
            if temp == []:
                kombinasi = faulthold.union(set(testcase[nilai]["Fault"]))
                temp.append(testcase[hold])
                temp.append(testcase[nilai])
                #temp.sort()
                pass
            elif len(kombinasi) < len(faulthold.union(set(testcase[nilai]["Fault"]))):
                temp = []
                kombinasi = faulthold.union(set(testcase[nilai]["Fault"]))
                temp.append(testcase[hold])
                temp.append(testcase[nilai])
                #temp.sort()
                pass
            nilai += 1
            pass
        pass
    gabungan = gabungan.union(kombinasi)
    #print(gabungan)
    #print(temp[0])
    #print(temp[1])
    testcase.remove(temp[0])
    testcase.remove(temp[1])
    optimal.remove(temp[0])
    optimal.remove(temp[1])
    optimal.insert(count,temp[0])
    count += 1
    optimal.insert(count,temp[1])
    count += 1
    temp = []
    pass

csv_columns = ['Test Case','Fault','Command']

try:
    print("creating file csv...")
    with open(f'2optimal_{namafile}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in optimal:
            writer.writerow(data)       
except IOError:
    print("I/O error")

f=open(f'universe_2optimal_{namafile}.txt','w')
print("creating file universe...")
for case in optimal:
    f.write(case["Command"]+'\n')
f.close()
print("file created")

print("Nilai APFD = ",calculateAPFD(optimal,jumlahfault))