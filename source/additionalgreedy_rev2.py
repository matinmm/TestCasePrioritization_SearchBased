import csv
import json
import os

namafile = input("Input Nama File : ")

def searchJumlahFault(testcase):
    jumlahfault = 0
    for case in testcase:
        for num in case["Fault"]:
            if num > jumlahfault:
                jumlahfault = num
                pass
            pass
        pass
    print(jumlahfault)
    return jumlahfault

try:
    f = open(f'{namafile}.json', "r")
    testcase = json.loads(f.read())
    jumlahfault = searchJumlahFault(testcase)
except IOError:
    print("Nama file yang diinputkan Salah")
    os._exit(1)

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


greedy = greedyAlgorithm(testcase)

tertinggi = set(greedy[0]["Fault"])
listadditional = []
gabungan = tertinggi
while(len(gabungan) != jumlahfault):
    nilai = 1
    temp = greedy[nilai]
    while (nilai < len(greedy) and greedy[nilai]["Fault"] != []):
        #print (gabungan)
        if len(gabungan.union(set(greedy[nilai]["Fault"]))) >= len(gabungan.union(set(temp["Fault"]))):
            temp = greedy[nilai]
            pass
        nilai += 1
    pass
    #print(temp)
    listadditional.append(temp)
    gabungan = gabungan.union(set(temp["Fault"]))
pass
#print (listadditional)
nilai = 1
for case in listadditional:
    greedy.remove(case)
    greedy.insert(nilai,case)
    nilai += 1
pass    

#print (greedy)
apfd = calculateAPFD(greedy,jumlahfault)
#print(apfd)

csv_columns = ['Test Case','Fault','Command']

try:
    print("creating file csv...")
    with open(f'additionalgreedy_{namafile}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in greedy:
            writer.writerow(data)       
except IOError:
    print("I/O error")

f=open(f'universe_additional_{namafile}.txt','w')
print("creating file universe...")
for case in greedy:
    f.write(case["Command"]+'\n')
f.close()
print("file created")

print("Nilai APFD = ",calculateAPFD(greedy,jumlahfault))