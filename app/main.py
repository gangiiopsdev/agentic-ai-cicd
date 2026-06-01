from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    ping_command = ['ping', host]
    try:
        output = subprocess.run(ping_command, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)