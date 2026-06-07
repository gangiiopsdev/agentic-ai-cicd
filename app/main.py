from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host input to prevent command injection
    host = sub.shlex_quote(host)
    try:
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'output': output.decode(), 'error': error.decode()}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return result