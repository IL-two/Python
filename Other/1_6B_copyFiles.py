# Контрольное задание 1_6B
# От Духно Ильи гр.124/20

import csv, logging, datetime

def directoryFile():
    file = input("Введите адрес cvs фйла: ")
    return file

def newFileTXT():
    file = input("Введите имя для txt файла: ")
    file = file + ".txt"
    txt = open(file, "w")
    logging.info("File %s created" % (file))
    return file

def newLogFile():
    timestring = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    logfile = 'python_' + timestring + '.log'
    logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s_%(levelname)s: %(message)s')


def getFile (file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            row = list(reader)
        logging.info("File %s read" % (file))
        file.close()
        return row
    except FileNotFoundError:
        logging.error("File %s noteFound" % (file))
        return 0

def copyFile (nameFile, list):
    cvsToTxt = open(nameFile, "a")
    for it in list:
        date = datetime.datetime.utcnow().time()
        cvsToTxt.write(str(date) + ": " + str(it) + "\n")
    logging.info("File %s copy" % (nameFile))

newLogFile()

file = directoryFile()
txt = newFileTXT()

lisrRead = getFile(file)
if (lisrRead != 0):
    copyFile(txt, lisrRead)