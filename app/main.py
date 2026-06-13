from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', '-c', '4', host]
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}