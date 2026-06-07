from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', subprocess.check_output(['echo', host], text=True).strip()]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout@app.get("/ping")def ping(host: str):
    try:
        status = safe_ping(host)
        return {'status': 'completed', 'output': status}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}