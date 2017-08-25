import os


wget1 = "wget http://kitti.is.tue.mpg.de/kitti/raw_data/2011_09_26_drive_"
unzip1 = "unzip "
del1 = "rm "
dash = "/"
cmd2 = "2011_09_26_drive_"
cmd3 = "_sync.zip"

#data.py
numbers = ["0001", "0017", "0029", "0052", "0070", "0002", "0018", "0035", "0056", "0079", "0019", "0036", "0005", "0057", "0084", "0020", "0039", "0059", "0086", "0011", "0023", "0046", "0060", "0091", "0013", "0027", "0048", "0061", "0015", "0028", "0051", "0064", "0009", "0014", "0022", "0032", "0087", "0093", "0095", "0096", "0104", "0106", "0113", "0117", "0119"]


## [synced+rectified data]
#http://kitti.is.tue.mpg.de/kitti/raw_data/2011_09_30_drive_0028/2011_09_30_drive_0028_sync.zip
for index in range(len(numbers)):
    number=numbers[index]
    wget = wget1+number+dash+cmd2+number+cmd3
    uzip = unzip1+cmd2+number+cmd3
    rmfile = del1+cmd2+number+cmd3
    print(wget)
    print(unzip)
    print(rmfile)
    k=os.system(wget)
    k=os.system(unzip)
    j=os.system(rmfile)


##[tracklets] 
#http://kitti.is.tue.mpg.de/kitti/raw_data/2011_09_26_drive_0001/2011_09_26_drive_0001_tracklets.zip

cmd3 = "_tracklets.zip"

for index in range(len(numbers)):
    number=numbers[index]
    wget = wget1+number+dash+cmd2+number+cmd3
    unzip = unzip1+cmd2+number+cmd3
    rmfile = del1+cmd2+number+cmd3
    print(wget)
    print(unzip)
    print(rmfile)
    k=os.system(wget)
    k=os.system(unzip)
    j=os.system(rmfile)
