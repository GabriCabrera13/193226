from threading import Thread, Lock
import threading
import time
mutex = threading.Lock()


def comedor():
    tenedores=0
    hilo_actual = threading.current_thread().getName()
    while True:
        print(f'los filosofos {hilo_actual} estan esperando')
        time.sleep(2)
        mutex.acquire()
        if tenedores==0:
            print(f'El filosofo {hilo_actual} ha tomado sus 2 tenedores')
            time.sleep(2)
            tenedores=2
        
        try:
            if tenedores==2:
                print(f'El filosofo {hilo_actual} ha comenzado a comer')
                time.sleep(2)
                tenedores=0
        finally:
            print(f'el filosofo {hilo_actual} ha terminado de comer')
            time.sleep(3)
            mutex.release()
            break

def main():

    filosofo1 = Thread(name='1',target=comedor, args=())
    filosofo2 = Thread(name='2',target=comedor, args=())
    filosofo3 = Thread(name='3',target=comedor, args=())
    filosofo4 = Thread(name='4',target=comedor, args=())
    filosofo5 = Thread(name='5',target=comedor, args=())
    

    filosofo1.start()
    filosofo2.start()
    filosofo3.start()
    filosofo4.start()
    filosofo5.start()
main()




        