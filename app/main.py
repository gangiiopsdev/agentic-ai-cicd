from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host):
        # Sanitize input to prevent injection
        safe_host = ''.join(c for c in host if c.isalnum() or c in ('-', '.', '_', ':'))
        try:
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = SafeSubprocess.ping(host)
    return {'status': 'completed', 'response': response}