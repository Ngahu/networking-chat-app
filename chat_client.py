import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name,sock):
    while not shutdown:
