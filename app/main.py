from fastapi import FastAPI
import subprocess
get_ip = 'ping -c 1 {}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    ip_parts = host.split('.')
    if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
        return {'error': 'Invalid IP address'}
    subprocess.call(get_ip.format(host), shell=True)
    return {'status': 'completed'}