from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = host.split('@')[-1]
        args = ['ping', '-c', '4', ip_address]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)