from xml.dom import minidom
from zipfile import ZipFile
import os
import settings
from multiprocessing import Pool
def move_(a):
    # for k in range(settings.count_zip):
    # for a in  k:
    your_path = a[1] + "pack" + str(a[0]) + ".zip"
    f = open(a[2], 'a')
    fl = open(a[3], 'a')
    if os.path.exists(your_path):
        # unzip files
        my_zipFile = ZipFile(your_path, 'r')
        my_zipFile.extractall(a[1])
        for i in range(settings.count_file_xml):
            name = a[1] + "data_" + str(i) + ".xml"
            print(name)
            xmldoc = minidom.parse(name)
            VarElement = xmldoc.getElementsByTagName('var')
            # id and level move to levels.csv
            f.write(VarElement[0].getAttribute('value') + ',' + VarElement[1].getAttribute('value') + '\n')

            ObjectElement = xmldoc.getElementsByTagName('object')
            # id and level move to objects.csv
            for element in ObjectElement:
                fl.write(element.getAttribute('name') + ',' + VarElement[0].getAttribute('value') + '\n')
            if os.path.isfile(name):
                os.remove(name)
    else:
        print(a[1] + "pack" + str(a[0]) + ".zip" + " is not correct")
    f.close()
    fl.close()
def make_csv():
    # try:
        # file levels.csv create
        if os.path.exists(settings.path_level_csv):
            path_level = settings.path_level_csv + "levels.csv"
        else:
            path_level = settings.path_level_csv + "levels.csv"
        f = open(path_level, 'w')

        # file objects.csv create
        if os.path.exists(settings.path_objects_csv):
            path_objects=settings.path_objects_csv + "objects.csv"
        else:
            path_objects = settings.path_objects_csv + "objects.csv"
        fl = open(path_objects, 'w')

        if os.path.exists(settings.path_zip):
            path=settings.path_zip
        else:
            path =""
        a = [[i, path,path_level,path_objects] for i in range(settings.count_zip)]
        f.close()
        fl.close()
        if __name__ == '__main__':
            with Pool(8) as p:
                p.map(move_, a)
    # except:
    #     print("There is error in creation csv file")
make_csv()
