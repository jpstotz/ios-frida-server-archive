# Download latest .deb file frida-server for iOS arm64
import os.path
from pathlib import Path
import cydiarepor
import urllib.request

repo_url = 'https://build.frida.re'

deb_list = cydiarepor.get_debs_from_cydiarepoURL(repo_url)

for deb in deb_list:
    file_name = deb['Filename']
    if 'iphoneos-arm64' in file_name:

        file = os.path.basename(file_name)
        if os.path.exists(file):
            print("{} already exists".format(file))
            exit(0)

        url = repo_url + '/' + file_name
        urllib.request.urlretrieve(url, file)

        print(deb)

exit(0)