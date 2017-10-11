import wget
import gzip


file_url = "https://s3.amazonaws.com/swrve-public/full_stack_programming_test/test_data.csv.gz"

#file_name = wget.download(file_url)

with gzip.open('./test_data.csv.gz', 'rb') as f:
    file_content = f.read()
    #print(file_content)


strFile = file_content.decode("utf-8")
#file123 = open("test.txt", "w")
#file123.write(strFile)

arrData = strFile.split("\n")

print (arrData)

data= arrData[1:]

print(data)
columnsStr = arrData[1]
columns = columnsStr.split(',')
print(columns)

index1 = columns[3]

print(str(index1))
