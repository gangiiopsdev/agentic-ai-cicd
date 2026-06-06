from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', quote(host)])

@app.get("/ping")
def ping_route(host: str):
    try:
        result = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}