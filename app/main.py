from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return None, str(e)
    except Exception as e:
        return None, str(e)

def validate_host(host):
    # Implement validation logic here (e.g., IP address range, domain name format)
    pass

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}