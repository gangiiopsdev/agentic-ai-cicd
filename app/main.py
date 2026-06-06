from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent shell injection
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout.decode(), result.stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'status': 'error', 'message': error}
        else:
            return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}