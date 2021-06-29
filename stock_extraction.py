from ib_insync import *
from bs4 import BeautifulSoup

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=2)

sub = ScannerSubscription(instrument='FUT.US',
                    locationCode='FUT.GLOBEX', 
                    scanCode='TOP_PERC_GAIN')
scanner = ib.reqScannerData(sub, [])
print(scanner)
 