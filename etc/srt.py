import argparse
import sys
import time
from datetime import datetime
from getpass import getpass
from random import randint

from SRTpy import Srt
from heconvert.converter import h2e

parser = argparse.ArgumentParser()
parser.add_argument('--id', type=lambda s: str(int(s)), required=True)
parser.add_argument('--password', type=str)
parser.add_argument('--dpt', type=str, required=True)
parser.add_argument('--arv', type=str, required=True)
parser.add_argument('--date', type=lambda d: datetime.strptime(d, '%Y%m%d').strftime('%Y%m%d'))
parser.add_argument('--hour', type=lambda h: datetime.strptime(h, '%H').strftime('%H0000'))

args = parser.parse_args()

id = args.id
password = args.password if args.password else getpass('password: ')
dpt = args.dpt
arv = args.arv
date = args.date
hour = args.hour

srt = Srt(id, password)
while True:
    print('검색: %s %s %s %s' % (dpt, arv, date, hour))
    trains = srt.search(h2e(dpt), h2e(arv), date, hour, include_no_seat=True)
    print('\t' + '\n\t'.join(map(str, trains)))
    for train in (train for train in trains if train.has_general_seat()):
        try:
            srt.reserve(train)
            print('예약완료: %s' % train)
        except Exception as e:
            print('예약실패: %s' % e)
    sys.stdout.flush()
    time.sleep(randint(5, 15))

