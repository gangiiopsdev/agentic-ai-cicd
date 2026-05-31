from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c in '_.-')
        try:
            output = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=False)
            return {'status': 'completed' if output.returncode == 0 else 'failed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)