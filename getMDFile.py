import os
FileList = []
FileNames = os.listdir("./book")
print(len(FileNames))
for i in FileNames:
    print(i[0:-15])

with open("./book/SUMMARY.md", "wb") as summaryfile:
    for i in FileNames:
        path1 = '*' + ' ' + '[' + i[0:-15] + '](' +'./' + i + ')'
        summaryfile.write(path1.encode('utf-8'))
        summaryfile.write('\r\n'.encode('utf-8'))

cmd = "gitbook epub ./book ./liushenleilei.epub"
os.system(cmd)



