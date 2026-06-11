from fastapi import FastAPI
import subprocess
def shell_quote(s):
    return ''.join(['\', c] if c in '\"$`' else c for c in s)

class SafePing:
    def ping(self, host: str) -> None:
        safe_host = shell_quote(host)
        subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    SafePing().ping(host)
    return {'status': 'completed'}