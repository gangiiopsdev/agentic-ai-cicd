from fastapi import FastAPI
import subprocess
global BLACKLISTED_HOSTS
BLACKLISTED_HOSTS = {'example.com', 'test.com'}  # Define a list of blacklisted hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in BLACKLISTED_HOSTS:
        return {"status": "error", "message": "Host is blacklisted"}
    else:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}