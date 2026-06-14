from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not host.strip().replace('.', '').isalnum():
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', shlex.quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except Exception as e:
        return str(e), ''

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}