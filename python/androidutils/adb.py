import os
import subprocess
import utils.systemUtils as util

def runSystemCommand(cmd, out=True):
    # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # for line in p.stdout.readlines():
    #     print line,

    with open(os.devnull, 'w')  as FNULL:
        try:
            if not out:
                ret = subprocess.call(cmd, shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
            else:
                ret = subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError:
            print 'failed to execute ret val :' + str(ret) + 'command : ' + cmd
        finally:
            FNULL.close()

    return ret

def runSystemCommandAndGetoutput(cmd, out=True):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    ret = p.wait()
    return ret

class adb:
    def __init__(self):
        self.name = 'adb'

    def shell(self,cmd,needoutput=False):
        adbshell = 'adb shell '
        command = adbshell + cmd
        #print command
        if needoutput:
            return runSystemCommandAndGetoutput(command,out=False)

        runSystemCommand(command)

    def sudoShell(self,cmd):
        sudocmd = 'su 0 '
        self.shell(sudocmd + cmd)

    def isConnected(self):
        return util.CONVERT_TO_C_RETURN(
            runSystemCommand('adb shell time', out=False))
