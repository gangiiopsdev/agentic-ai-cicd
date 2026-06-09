from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        if not host.strip():
            raise ValueError('Host parameter cannot be empty or contain only whitespace')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)