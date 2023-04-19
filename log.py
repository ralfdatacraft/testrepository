#Modul importieren und Basiseinstellung für den Log-Eintrag festlegen
import logging

fn = 'beispiel.log'

logging.basicConfig(filename=fn,
                    filemode='w',
			        format='%(asctime)s - %(message)s',
			        level=logging.INFO)

#In 4 Stufen festgehalten:
#DEBUG, WARNING, ERROR, CRITICAL
logging.debug('detaillierte Informationen')
logging.warning('Programm läuft, aber etwas ungewöhnliches ist aufgetreten, z.B. wenig Speicherplatz')
logging.error('Einige Funktionen konnten nicht ausgeführt werden')
logging.error('Einige Funktionen konnten nicht ausgeführt werden')
logging.error('Einige Funktionen konnten nicht ausgeführt werden')
logging.error('Einige Funktionen konnten nicht ausgeführt werden')
logging.critical('kritischer Fehler, das Programm wurde beendet')

def divisor(x=1,y=0):
    try:
        print(x/y)
        logging.warning('Das sieht super aus und läuft perfekt')
    except:
        print('FEHLER FEHLER FEHLER')
        logging.error('NICHT DURCH 0 TEILEN AHHHHHHHHHHHHHHHHHHH')

divisor(1,2)
divisor(1,0)