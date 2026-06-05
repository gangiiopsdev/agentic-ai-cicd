from fastapi import FastAPI
import subprocess
cimport os
cimport sys

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}