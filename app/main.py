from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        if not host.isalnum():  # Basic input validation
            raise ValueError('Invalid host name')
        args = ['ping', host]  # Use list to avoid shell injection
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}