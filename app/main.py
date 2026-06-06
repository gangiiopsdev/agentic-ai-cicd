from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Preventive controls
# 1. Validate input: Ensure that the host parameter is a valid hostname or IP address.
# 2. Use absolute paths for commands: Specify the full path to the ping executable if possible.
# 3. Limit privileges: Run the application in a restricted environment with limited permissions.