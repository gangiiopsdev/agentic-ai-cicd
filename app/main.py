from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        # Validate and sanitize the input to prevent command injection
        if not host.isalnum() or len(host) > 255 or ' ' in host or '\\' in host or ';' in host or '|' in host or '&' in host or '>' in host or '<' in host or '`' in host or '$' in host:
            return 'Invalid host'
        try:
            result = subprocess.run(['ping', subprocess.check_output(f'echo -n {host}', shell=True, text=True).strip()], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return SafePing.run(host)