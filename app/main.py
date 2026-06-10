from fastapi import FastAPI
import subprocess
import shlex

global ping_command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input
        safe_host = shlex.quote(host)
        ping_command = ['ping', safe_host]
        result = subprocess.run(ping_command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
ping_command = ['ping', 'host']