from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in '._-')

cmd = ['ping', '-c', '4', '{}'.format(sanitize_input(host))]
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}