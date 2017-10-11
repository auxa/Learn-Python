import wget
import gzip


def removeEmpty(dataSet):
    dataSet.remove("")
    return dataSet

def searchForQuantity( wVal, hVal, dataSet):
    wIndex = columns.index('device_width')
    hIndex =columns.index('device_height')
    frequency =0
    for data in dataSet:
        if data[wIndex] == str(wVal) and data[hIndex] == str(hVal):
            frequency +=1
    return frequency

def splitIt(dataSet):
    newData = []
    for data in dataSet:
        datum = data.split(',')
        newData.append(datum)

    return newData

def sumDollars(dataSet):
    dollars=0;
    index = columns.index('spend')
    for data in dataSet:
        dollars = dollars +  float(data[index])
    return dollars





file_url = "https://s3.amazonaws.com/swrve-public/full_stack_programming_test/test_data.csv.gz"

#file_name = wget.download(file_url)

with gzip.open('./test_data.csv.gz', 'rb') as f:
    file_content = f.read()
    #print(file_content)


strFile = file_content.decode("utf-8")
#file123 = open("test.txt", "w")
#file123.write(strFile)

arrData = strFile.split("\n") # Splits file into rows
arrData= removeEmpty(arrData)  #removes empty rows

arrData = splitIt(arrData)

columns = arrData[0]    #denotes this as the row with the coulmn names
data= arrData[1:]   #rest of data without column names



res = searchForQuantity(640,960, data)
spend = sumDollars(data)
print(spend)
print(res)
index1 = columns[3]

print(columns)
print(len(data))
