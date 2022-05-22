import os
import subprocess
import argparse
from geopy.geocoders import Nominatim

def main():
    #TODO add option to scan multiple images
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-a", "--all", nargs="?", const=os.getcwd(), help="Scans all.")
    parser.add_argument("-s", "--single", help="Scans an image.")
    parser.add_argument("-l", "--list", nargs="?", const=os.getcwd(), help="Lists images.")
    args = parser.parse_args()
    if args.all:
        check_all(args.all)
    elif args.single:
        check_single(args.single)
    elif args.list:
        check_dir(args.list)


def check_single(img):
    '''get exif data and location from the image'''
    try:
        gps = get_exif(img)
    except:
        return 1
    geolocator = Nominatim(user_agent="exif")
    location = geolocator.reverse(get_dec(gps[0])+","+(get_dec(gps[1])))
    print(location)

def check_all(dir):
    '''scan all the images from the directory'''
    #TODO add more file formats
    with os.scandir(dir) as dir:
        for entry in dir:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(entry.name + ' - ', end='')
                check_single(entry.name)

def check_dir(dir):
    '''get lists of images from the directory'''
    #TODO add more file formats
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
