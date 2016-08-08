# GooglePlayDownloader

GooglePlayDownloader is a graphical software to download APKs from the Google Play store.

I ever wanted to get applications from the Google Play store but didn't like my android AOSP system being tainted by Google root services neither being filed in the Google account database.

# License
The software is based on :
- googleplay-api to interact with Google PlayStore (https://github.com/egirault/googleplay-api/) BSD license
- androguard to read info info from local APKs on disk (http://code.google.com/p/androguard/) LGPL license
These libs are packaged in the src/ext_libs folder for user convenience but are not part of this project.

The GUI (googleplaydownloader.py) is under AGPL licence (copyright Tuxicoman)

# Requirements

  Dependencies are:
  - python-requests (>=0.12)
  - python-pyasn1 for SSL connections
  - python-wxgtk (>=2.8) for the GUI
  - python2 (>=2.7)

  You can install them through your package manager. For example on Debian :
  # apt-get install python-wxgtk2.8 python-requests python-pyasn1

# Use

## Use Debian package
  The Debian packages are in the packages/ folder.
  
  Install it:
  
  # dpkg -i googleplaydownloader.deb

  Solve packages dependencies:
  
  # apt-get install -f

## Manual launch

  To launch the software form this folder, just do :
  
  $ python googleplaydownloader/googleplaydownloader.py

## Build Debian package

  Build a debian package (you can also download the prebuild .deb from the website):
  
  $ build_debian_pachage.sh

  

Enjoy !