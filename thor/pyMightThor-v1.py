# thor // 192.168.192.161:22
# root@thor:/opt/pyMightyThor# cat pyMightThor.py
from glob import glob
import os, os.path

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def spv(sVarName, oVar):
    print(str(sVarName) + ": " + str(oVar) + " " + str(type(oVar)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sTopDirPath = '/media/qnap/'
    spv('sTopDirPath', sTopDirPath)
    lDirPaths = glob(sTopDirPath + "*/") # recursive= True
    spv('lDirPaths', lDirPaths)
    for sDirPath in lDirPaths:
        spv('sDirPath', sDirPath)
        if 'thor_' in sDirPath:
            #print('HIT!')
            lSubDirPaths = glob(sDirPath + "*/") # recursive=False
            spv('lSubDirPaths', lSubDirPaths)
            for sSubDirPath in lSubDirPaths:
                spv('sSubDirPath', sSubDirPath)
                iNumOfFilesInSubDirPath = len([name for name in os.listdir(sSubDirPath) if os.path.isfile(os.path.join(sSubDirPath, name))])
                spv('iNumOfFilesInSubDirPath', iNumOfFilesInSubDirPath)
                if iNumOfFilesInSubDirPath == 0:
                    #print('HIT!')
                    #input('ENTER!')
                    try:
                        os.rmdir(sSubDirPath)
                        print("Directory "+sSubDirPath+" has been removed successfully")
                    except OSError as error:
                        print(error)
                        print("Directory "+sSubDirPath+" can not be removed")
                    #input('ENTER!')
                else:
                    print('MISS!')
            iNumOfFilesInDirPath = len([name for name in os.listdir(sDirPath) if os.path.isfile(os.path.join(sDirPath, name))])
            if iNumOfFilesInDirPath == 0:
                try:
                    os.rmdir(sDirPath)
                    print("Directory " + sDirPath + " has been removed successfully")
                except OSError as error:
                    print(error)
                    print("Directory " + sDirPath + " can not be removed")


