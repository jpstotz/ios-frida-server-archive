# Download latest .deb file frida-server for iOS arm64
import os.path
from pathlib import Path
import cydiarepor
import urllib.request

repo_url = 'https://build.frida.re'

deb_list = cydiarepor.get_debs_from_cydiarepoURL(repo_url)

for deb in deb_list:
    file_name = deb['Filename']
    print(file_name)
    if 'iphoneos-arm' not in file_name:
        continue
    file = os.path.basename(file_name)
    subdir = Path(file).stem.rpartition('_')[2]
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    file = os.path.join(subdir, file)
    if os.path.exists(file):
        print("{} already exists".format(file))
        continue

    print("Saving {}".format(file))
    url = repo_url + '/' + file_name
    urllib.request.urlretrieve(url, file)

    print(deb)

exit(0)
