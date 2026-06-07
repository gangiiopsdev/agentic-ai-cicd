from fastapi import FastAPI
import subprocess

def execute_safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

class FastAPIApp(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        return execute_safe_ping(host)

app = FastAPIApp()