import os

import socket
import traceback
from multiprocessing import Pool
import pandas
# from concurrent.futures import ThreadPoolExecutor

def connect_t(ipaddr=None, port=None):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        # s.connect(('220.181.38.148', 80))
        s.connect((ipaddr, port))
        s.close()
        res = 'success'
    except Exception:
        traceback.print_exc()
        res = 'failed'

    return (ipaddr, port, res)


def acceptR(n=None, f=None, ip=None, w=None):
    futureList = []
    # with ThreadPoolExecutor(max_workers =n) as executor:
    with Pool(processes=n) as executor:

        # processIP
        if f == 'ping':

            ip1 = ip.split('-')[0]
            ip2 = ip.split('-')[1]

            ipList = []
            iparray1 = ip1.split('.')
            iparray2 = ip2.split('.')

            start = iparray1.pop()
            print(start)
            end = iparray2.pop()
            print(end)

            index = int(start)
            while index <= int(end):
                iparray1.append(str(index))
                ipList.append('.'.join(iparray1))
                iparray1.pop()
                index = index + 1

            for ipaddr in ipList:
                # future = executor.submit(connect_t, ipaddr, 80)
                # futureList.append(future.result())
                future = executor.apply_async(connect_t, args=(ipaddr, 80))
                futureList.append(future.get())

            # return futureList

        else:
            index = 0
            portList = []
            while index <= 5:
                portList.append(index)
                index = index + 1

            for port in portList:
                # future = executor.submit(connect_t, ip, port)
                # futureList.append(future.result())
                future = executor.apply_async(connect_t, args=(ip, port))
                futureList.append(future.get())

        print(futureList)
        if not w is None:
            try:
                dataList = pandas.DataFrame(data=futureList)
                dataList.to_csv('./' + w, mode='a', encoding='utf8', index=False, header=['ip','port','result'])
            except Exception:
                traceback.print_exc()
        return futureList

    # return super().recvfrom_into(buffer, nbytes, flags)


if __name__ == '__main__':
    list = acceptR(n=4,f='ping',ip='220.181.38.148-220.181.38.150',w='ip.csv')
    print(list)

    list2 = acceptR(n=4, f='tcp', ip='220.181.38.148',w='ip2.csv')
    print(list2)
