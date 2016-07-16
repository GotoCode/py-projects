'''
A simple python script to find out
the ip of the current system using 'ifconfig'

WARNING: will work as is with Linux / Mac OS X,
         but requires some changes when working
         on a Windows system
'''


import commands
import re


# name of ip retrieval command
cmd_name = 'ifconfig'


def main():
    
    status, output = commands.getstatusoutput(cmd_name)

    # if status != 0, call to cmd failed
    if (status):
        raise Exception('Could not retrieve system ip address')

    # on successful call to ifconfig...
    else:
        # ...extract ip address from output
        ip_addr = re.search(r'192\.\d+\.\d+\.\d+', output)
        
        print 'Current IP address:', ip_addr.group(0)


if __name__ == '__main__':
    main()