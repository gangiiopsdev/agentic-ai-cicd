from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> dict:
    if not host or ' ' in host or '\' in host or '"' in host or ';' in host or '>' in host or '<' in host or '|' in host or '&' in host:
        return {'error': 'Invalid input'}, 400
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return result[0], 200 if isinstance(result[0], dict) and 'status' in result[0] else result[1]
    except Exception as e:
        return {'error': str(e)}, 500