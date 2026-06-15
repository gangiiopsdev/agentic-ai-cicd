from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Validate and sanitize the host input
        if not host.replace('.', '').isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)