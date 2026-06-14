from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using Popen instead of call for better control and security
        subprocess.Popen(['ping', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)