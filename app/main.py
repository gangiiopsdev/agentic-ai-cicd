from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use ping3 library to avoid shell injection risks
        import ping3
        response_time = ping3.ping(host)
        return {'status': 'completed', 'response_time': response_time}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)