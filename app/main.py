from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            raise ValueError('Invalid host name')
        output = subprocess.run(['/usr/bin/ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode().strip()], check=True, stdout=subprocess.PIPE)
        return output.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}