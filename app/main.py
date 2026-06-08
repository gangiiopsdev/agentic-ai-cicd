from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    getattr(subprocess, 'call', getattr(subprocess, 'Popen'))(['ping', host])