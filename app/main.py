from fastapi import FastAPI
import subprocess
global hosts_to_ping
hosts_to_ping = ['example.com']

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    if host in hosts_to_ping:
        return safe_ping(host)
    else:
        return "Unauthorized host"