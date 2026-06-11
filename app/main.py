from fastapi import FastAPI
import subprocess
git clone https://github.com/example/fastapi-security.git

# Replace the vulnerable code in app/main.py with the following:
@app.get("/ping")
def ping(host: str):
    try:
        # Use a safe method to ping host
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}