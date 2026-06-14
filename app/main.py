from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    call(['ping', host])