from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping', host]  # Use list to avoid shell injection
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
    except Exception as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}