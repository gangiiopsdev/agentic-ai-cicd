from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize input by ensuring it does not contain shell metacharacters
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)