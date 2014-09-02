#!/bin/bash

set -e
set -x

for module in ljtemp zwave brewery webserver ;
do
	cd $module
        sudo rm -Rf build
	sudo rm -Rf /usr/local/lib/python2.7/dist-packages/$module
        sudo python setup.py install
        cd ..
done

