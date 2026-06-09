from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def validate_host(host: str) -> bool:
    # Basic validation to ensure the input is a valid hostname or IP address
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            response = safe_ping(host)
            return {'status': 'completed', 'response': response}
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host input'}