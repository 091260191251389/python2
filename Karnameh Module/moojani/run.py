from main import karnameh
file = open("result.txt" , "a")
result = karnameh()
for i in result:
    output = str(result[i]) + "\n"
    file.write(output)
     
file.close()