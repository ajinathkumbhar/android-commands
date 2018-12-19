#!/usr/bin/python

import os
import subprocess
from androidutils.adb import adb

adb = adb()
def main():
    if not adb.isConnected():
        print 'Please connect device or check adb permission'
        return
    print 'Product name         : ',
    adb.shell('getprop ro.product.name',needoutput=True)
    print 'Project name         : ',
    adb.shell('getprop ro.boot.project_name',needoutput=True)
    print 'Factory Serial No.   : ',
    adb.shell('getprop ro.serialno',needoutput=True)
    print 'HW Serial No.        : ',
    adb.shell('getprop ro.serialno.hw',needoutput=True)
    print 'Build Details        : ',
    adb.shell('getprop ro.build.display.id',needoutput=True)
    print 'Build fingerprint    : ',
    adb.shell('getprop ro.build.fingerprint',needoutput=True)
    print 'Build date           : ',
    adb.shell('getprop ro.build.date',needoutput=True)
    print 'Kernel Build date    : ',
    adb.shell('getprop ro.bootimage.build.date',needoutput=True)
    print 'MPSS Build baseband  : ',
    adb.shell('getprop gsm.version.baseband',needoutput=True)
    print 'MPSS Build baseband1 : ',
    adb.shell('getprop gsm.version.baseband1',needoutput=True)
    print 'GMS Build 	     : ',
    adb.shell('getprop ro.com.google.gmsversion',needoutput=True)
    print 'Security Patch Level : ',
    adb.shell('getprop ro.build.version.security_patch',needoutput=True)



if __name__ == '__main__':
    main()
