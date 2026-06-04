from fastapi import FastAPI
import subprocess
call = ['ping', host]
if subprocess.call(call, shell=False) != 0:
    raise Exception('Ping failed')