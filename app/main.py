from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using subprocess.Popen instead of subprocess.call for better security
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping(host)}