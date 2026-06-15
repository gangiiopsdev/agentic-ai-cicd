from fastapi import FastAPI
import subprocess
cimported = set(['ping'])

app = FastAPI()

def safe_ping(host):
    try:
        # Use a whitelist for hosts to avoid arbitrary command execution
        allowed_hosts = ['example.com', 'localhost']
        if host not in allowed_hosts:
            raise ValueError('Host is not allowed')
        subprocess.run([cmd for cmd in imported if cmd in host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}