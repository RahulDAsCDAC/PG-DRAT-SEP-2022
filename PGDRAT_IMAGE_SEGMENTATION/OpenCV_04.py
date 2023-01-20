import os
directory = "Capture_Image"
parent_dir = "C:/RD_Works/PGDRAT/PGDRAT_IMAGE_SEGMENTATION"
path = os.path.join(parent_dir, directory)
if os.path.isdir(path) == True:
    print('Folder Exists')
    print("Directory '% s' created" % directory)
else:
    os.mkdir(path)