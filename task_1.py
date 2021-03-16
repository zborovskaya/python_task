from xml.dom import minidom
from zipfile import ZipFile
import os
import random
import settings
import utils

#xml file create
def make_file_xml(name):
    try:

        doc = minidom.Document()

        # tag root create
        root = doc.createElement('root')
        doc.appendChild(root)

        # tag var create
        var=doc.createElement('var')
        var.setAttribute('value', utils.generate_random_string_lowercase(8))
        var.setAttribute('name', 'id')
        root.appendChild(var)

        # tag var create
        var=doc.createElement('var')
        var.setAttribute('value', str(random.randint(1,100)))
        var.setAttribute('name', 'level')
        root.appendChild(var)

        # tag objects create
        objects=doc.createElement('objects')
        i=0
        while i<random.randint(1,10):
            object_1 = doc.createElement('object')
            object_1.setAttribute('name', utils.generate_random_string_uppercase(8))
            objects.appendChild(object_1)
            i=i+1
        root.appendChild(objects)

        #writing to file

        xml_str = doc.toprettyxml(indent="  ")
        with open(name, "w") as f:
            f.write(xml_str)
            f.close()
    except:
        print("xml file created with an error ")


#zip create
def make_zip(path_zip):
    try:
        for k in range(settings.count_zip):
            name_zip= path_zip+"pack" + str(k) + ".zip"
            print(name_zip)
            with ZipFile(name_zip, "w") as newzip:
                for i in range(settings.count_file_xml):
                    name = "data_" + str(i) + ".xml"
                    make_file_xml(name)
                    newzip.write(name)
                    if os.path.isfile(name):
                        os.remove(name)
    except:
        print("zip created with an error ")


if os.path.exists(settings.path_zip):
    make_zip(settings.path_zip)
else:
    make_zip("")
