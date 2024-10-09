"""Tercer intento del algoritmo de Dekker"""
import logging
import threading
import time

signal = [False, False]

def  process(num):
    """Target function for threads"""
    logging.info('Thread %d: starting', num)
    signal[num] = True
    while signal[not num]:
        logging.info('Thread %d: waiting', num)
        time.sleep(0.5) # Simulate waiting
    logging.info('Thread %d: critical section', num)
    time.sleep(5) # Simulate critical section
    signal[num] = False
    logging.info('Thread %d: non critical section', num)
    logging.info('Thread %d: finishing', num)


if __name__ == '__main__':
    FORMAT = "%(asctime)s: %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")
    t0 = threading.Thread(target=process, args=(0,))
    t1 = threading.Thread(target=process, args=(1,))
    logging.info('Main: starting')
    t0.start()
    t1.start()
    t0.join()
    t1.join()
    logging.info('Main: finishing')
