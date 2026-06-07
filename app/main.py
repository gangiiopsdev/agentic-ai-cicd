from fastapi import FastAPI
import subprocess
cimport socket
def ping(host: str):
    try:
        socket.gethostbyname(host)
        return {'status': 'completed'}
    except socket.gaierror:
        return {'status': 'failed'}