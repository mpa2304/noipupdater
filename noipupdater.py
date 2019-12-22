from requests import get
import socket
import logging
from datetime import datetime

config = {
    "username": "NO IP username (email)",
    "password": "NO IP password",
    "hostname": "NO IP domain to check",
    "logfile": "Absolute path to a file for logging"
}

ip = get('https://api.ipify.org').text
urlIp = socket.gethostbyname(config['hostname'])
noipUpdateUrl = "http://" + config["username"] + ":" + config["password"] + \
    "@dynupdate.no-ip.com/nic/update?hostname=" + \
    config["hostname"] + "&myip=" + ip


def logResponse(res):
    logging.basicConfig(filename=config['logfile'], level=logging.DEBUG)
    datetimeStr = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logging.info(datetimeStr + ' ' + res)


if ip != urlIp:
    changeIpRes = get(noipUpdateUrl).text + ' From IP: ' + \
        urlIp + ' to IP: ' + ip
    logResponse(changeIpRes)
