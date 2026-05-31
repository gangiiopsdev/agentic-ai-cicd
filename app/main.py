from fastapi import FastAPI
import subprocess

def get_ip(host):
    # Secure implementation using check_output and avoiding shell=True
    result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
    return result

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = get_ip(host)
        return {'status': 'completed', 'result': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}