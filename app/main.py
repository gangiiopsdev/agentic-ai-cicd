from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', str(host)], stderr=subprocess.STDOUT, shell=True)
        return True, output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return False, str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    result, message = ping_safe(host)
    if not result:
        return {'status': 'failed', 'message': message}
    else:
        return {'status': 'completed', 'result': message}