import logparser

logfile = open('apache_logs','r')

ipcounter = {}

for logline in logfile:

    logparts = logparser.parser(logline)

    remotehost = logparts['host']

    if remotehost not in ipcounter:

        ipcounter[remotehost] = 1

    else:

        ipcounter[remotehost] += 1

logfile.close()

def get_ip(item):

    return item[1]

for item in sorted(ipcounter.items(),key=get_ip,reverse=True):

    ip,freq = item

    print(f'{ip:60} - {freq}')

