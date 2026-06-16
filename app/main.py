from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr.strip())
        return True
    except Exception as e:
        print(f'Ping failed: {e}')
        return False

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}