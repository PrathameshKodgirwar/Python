import os
import shutil

for i in os.listdir(r'C:\\Users\\Prathamesh\\Desktop\\Bizmetric Python\\'):
    fnm=r'C:\\Users\\Prathamesh\\Desktop\\Bizmetric Python\\'+i
    #sz=(os.stat('E:\\Python\\Bizmetric python\\'+i).st_size)/1024
    sz=os.stat(fnm).st_size/1000
    print(f'{i} {sz} KB')

    if sz<=30:
        print("Moving...",i)
        shutil.move('C:\\Users\\Prathamesh\\Desktop\\Bizmetric Python\\','D:\\Dummy')
    elif sz<=70:
        print("Moving...",i)
        shutil.move('C:\\Users\\Prathamesh\\Desktop\\Bizmetric Python\\','D:\\Dummy2')
    else:
        print("Moving...",i)
        shutil.move('C:\\Users\\Prathamesh\\Desktop\\Bizmetric Python\\','D:\\Dummy3')