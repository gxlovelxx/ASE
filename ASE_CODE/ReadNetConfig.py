filepathname_net = './netconfig.txt'

def ReadNetConfig(filepathname):
    pos = []
    allconfig = []
    count = 0
    with open(filepathname, 'r') as file_to_read:
        for f in file_to_read:
            f = f.strip()
            listconfig = f.split("=")
            print(listconfig)
            allconfig.append(listconfig[1])
        print(allconfig)
    return allconfig
if __name__ == '__main__':
    ReadNetConfig(filepathname_net)