import os
import sys
import subprocess
from geopy.geocoders import Nominatim

#img = sys.argv[1]


    # while True:
    #     img = sys.argv[1]
    #     if img == 'quit': break
#sys.argv[1]

def main():
    img = sys.argv[1]
    if img == '-h':
        print('-a = scan all entries\n-d, -d PATH: show the image files in the directory')
    elif img == '-a':
        if len(sys.argv) < 3:
            check_all(os.getcwd())
        else:
            try:
                check_all(sys.argv[2])
            except FileNotFoundError:
                print('Please enter a valid path.\nType -h for help')
    elif img == '-d':
        if len(sys.argv) < 3:
            check_dir(os.getcwd())
        else:
            try:
                check_dir(sys.argv[2])
            except FileNotFoundError:
                print('Please enter a valid path.\nType -h for help')
    else:
        check_single(img)


def check_single(img):
    try:
        gps = get_exif(img)
    except:
        return 1
    geolocator = Nominatim(user_agent="exif")
    location = geolocator.reverse(get_dec(gps[0])+","+(get_dec(gps[1])))
    print(location)

def check_all(dir):
    with os.scandir(dir) as dir:
        for entry in dir:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(entry.name + ' - ', end='')
                check_single(entry.name)

def check_dir(dir):
    with os.scandir(dir) as dir:
        for entry in dir:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(entry.name)


def get_exif(file):
    '''get exif data from the file'''
    raw = subprocess.check_output(['exiftool', '-gpsposition', file])
    exif = "".join(map(chr, raw))
    gps = exif[34:]
    return gps.split(',')
    
def get_dec(loc):
    '''format exiftool data to be used by geopy'''
    directions = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    dec = loc.replace(u'deg', '').replace("'", '').replace('"', '')
    dec = dec.split()
    dir = dec.pop()
    return str((int(dec[0])+float(dec[1])/60.0+float(dec[2])/3600.0) * directions[dir])


main()
if __name__ == 'main':
    main()
