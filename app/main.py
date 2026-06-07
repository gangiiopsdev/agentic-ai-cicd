from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Ensure host input does not include shell metacharacters
        if any(char in host for char in (';', '&', '|', '<', '>', '`', '$', '{', '}', '\')):
            raise ValueError('Invalid characters in hostname')
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}