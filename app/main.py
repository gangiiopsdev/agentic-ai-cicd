from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        return True
    return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Vulnerable implementation
    if safe_ping(host):
        subprocess.call(['ping', f'192.168.1.{host}'])  # Assuming a fixed IP range for demonstration purposes
    return {'status': 'completed'}