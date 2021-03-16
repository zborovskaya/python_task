from xml.dom import minidom
from zipfile import ZipFile
import os
import settings
from multiprocessing import Pool
def move_(path,f,fl):
    for k in range(settings.count_zip):
        your_path = path + "pack" + str(k) + ".zip"
        if os.path.exists(your_path):
            # unzip files
            my_zipFile = ZipFile(your_path, 'r')
            my_zipFile.extractall(path)
            for i in range(settings.count_file_xml):
                name = path + "data_" + str(i) + ".xml"
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
            print(path + "pack" + str(k) + ".zip" + " is not correct")
def make_csv():
    # try:
        # file levels.csv create
        if os.path.exists(settings.path_level_csv):
            f= open(settings.path_level_csv + "levels.csv",'w')
        else:
            f = open("levels.csv", 'w')

        # file objects.csv create
        if os.path.exists(settings.path_objects_csv):
            fl = open(settings.path_objects_csv + "objects.csv",'w')
        else:
            fl = open("objects.csv", 'w')

        if os.path.exists(settings.path_zip):
            path=settings.path_zip
        else:
            path =""
        move_(path,f,fl)
        f.close()
        fl.close()
    # except:
    #     print("There is error in creation csv file")
make_csv()