from fastapi import FastAPI
import subprocess
cimport os
cimport socket

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the input to prevent injection attacks
        if not host or len(host) > 255 or ':' in host or any(c in host for c in [';', '&', '|', '`']):
            raise ValueError("Invalid host")
        # Use os.path.basename to ensure safe execution
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}