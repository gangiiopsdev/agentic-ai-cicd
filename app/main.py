from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Using check_output to avoid shell injection risks
        output = subprocess.check_output(['ping', host], timeout=5, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/ping")
def ping(host: str):
    # Using a safe function to handle the ping command
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}