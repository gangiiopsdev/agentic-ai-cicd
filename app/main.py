from fastapi import FastAPI
import subprocess
def escape_input(input_string):
    return input_string.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}