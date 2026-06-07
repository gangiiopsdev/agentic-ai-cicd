from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip() and all(c in '0123456789.' for c in host):  # Basic validation of IP address format
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')
            return False
    else:
        raise ValueError('Invalid host input')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}