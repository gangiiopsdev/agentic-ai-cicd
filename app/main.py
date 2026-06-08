from fastapi import FastAPI
import subprocess
global hosts_list
hosts_list = ["example.com", "test.com"]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in hosts_list:
        try:
            result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}