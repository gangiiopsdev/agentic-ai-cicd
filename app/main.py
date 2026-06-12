from fastapi import FastAPI
import subprocess
cimport = False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not cimport:
        cimport = True
        try:
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}