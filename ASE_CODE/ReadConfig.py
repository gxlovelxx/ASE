import ParameterConfig as PC
import pandas as pd
filepathname = './config.txt'

DF_config = pd.read_csv(filepathname,sep="\t")
print(DF_config.head(16))
print(DF_config.columns)

DataType_df = DF_config.groupby("DataType")

print(DataType_df)
#print(DF_config.groupby("DataType").count())
#print(DF_config.groupby("DataType").head(6))

for name,group in DF_config.groupby("DataType"):
    print(name)
    print(type(group))
    print(group.head())
    # for i in group:
    #      print(i)







def ReadConfig(filepathname):
    #filename = './jizaigetway.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
    pos = []
    allconfig = []
    count = 0
    with open(filepathname, 'r') as file_to_read:
        #print(len(file_to_read))
        #linescount = len(file_to_read.readlines())
        #print(linescount)
        for f in file_to_read:
            #lines = file_to_read.readline() # 整行读取数据
            #print(lines)
            listconfig = f.split("\t")
            print(listconfig)
            #print(type(listconfig))
            allconfig.append(listconfig)
            #print(listconfig[6])
            count = count + 1
        #print(count)
        #print(allconfig)
    return count,allconfig

#获取参数属性
def Getconfig():
    allconfig = []
    count, myconfig = ReadConfig(filepathname)

    print(myconfig)
    #print(len(myconfig))
    for i in range(count):
        if i > 0:
            #paraobj = myconfig[i][1]
            #print(paraobj)
            paraobj = PC.ParameterConfig()
            paraobj.ParameterName = myconfig[i][1]
            paraobj.Lsb = myconfig[i][5]
            paraobj.Msb = myconfig[i][6]
            paraobj.StartWord = myconfig[i][8]
            paraobj.EndWord = myconfig[i][9]
            paraobj.InitialFrame = myconfig[i][11]
            paraobj.FrameIncrement = myconfig[i][12]
            paraobj.LsbRes = myconfig[i][13]
            paraobj.DataType = myconfig[i][14]
            paraobj.Bias = myconfig[i][15]
            #print(paraobj.DataType)
            allconfig.append(paraobj)
    return allconfig

if __name__ == '__main__':
    all = Getconfig()
    #print(all)