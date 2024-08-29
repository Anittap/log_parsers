import logparser

logfile = open('apache_logs','r')

statuscounter = {}

for logline in logfile:

    logparts = logparser.parser(logline)

    status = logparts['status']

    if status not in statuscounter:

        statuscounter[status] = 1

    else:

        statuscounter[status] += 1

logfile.close()

print(statuscounter)
