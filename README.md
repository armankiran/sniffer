# sniffer

A Basic Python script to automate [ExifTool](https://github.com/exiftool/exiftool) for personal use.

## usage
[ExifTool](https://github.com/exiftool/exiftool) has to be in the same path as sniffer. Otherwise, it can be changed by setting EXIF_PATH variable to ExifTool location.\
-s, --single /PATH: to scan a single image and get GPS location.\
-a, --all /PATH: to scan all the images in the PATH location. If no path is specified, gets GPS locations of the images in the sniffer's directory one by one.\
-l, --list /PATH: lists the scannable images in the PATH, If no PATH is specified, it will list the images in the sniffer's directory.\
Example usage in Windows: python sniffer.py -s image.jpg

## requirements
[ExifTool](https://github.com/exiftool/exiftool)
[GeoPy](https://geopy.readthedocs.io/)
