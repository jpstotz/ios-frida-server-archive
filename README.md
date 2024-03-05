# Download iOS frida-server

The Frida Cydia repository `https://build.frida.re` does only provide the latest version of frida-server.
The frida-server releases are only published on thois server and can not be found on the frida releases page.

Sometimes the latest frida-server version doesn't work as expected, therefore it would be useful to have some sort of archove of older frida-server versions.
Otherwise you have to build them on your own. 

This project allows to download (and archive) frida-server arm64 .deb installation packages, so older frida-server versions can be installed and used on iOS.

# Execution

    python ios-frida-server-download.py

Thois will download the recent version of `re.frida.server_*_iphoneos-arm64.deb` from https://build.frida.re if it does not yet exist in the local file-system.

# Dependencies

This projects depends on the project `cydiarepor` https://github.com/4ch12dy/cydiarepor.
The necessary code is already included. 