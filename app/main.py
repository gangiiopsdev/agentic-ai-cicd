from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def get_ping(host: str):
    return ping(host)