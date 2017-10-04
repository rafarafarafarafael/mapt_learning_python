allertSystem = 'email'
errorSeverity  = 'critical'
errorMessage = 'OMG! Something terrible happened!'

def sendMail(address=None, message=None):
    print('Dear ' + address)
    print(errorMessage)

if allertSystem == 'console':
    print(errorMessage)
elif allertSystem == 'email':
    if errorSeverity == 'critical':
        sendMail('admin@example.com', errorMessage)
    elif errorSeverity == 'medium':
        sendMail('support1@example.com', errorMessage)
    else:
        sendMail('support2@example.com', errorMessage)
