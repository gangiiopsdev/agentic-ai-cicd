from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation with shell=False and command line argument quoting
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)