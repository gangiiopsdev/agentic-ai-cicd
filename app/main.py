from fastapi import FastAPI
import subprocess
generate_random_hex = lambda: ''.join([random.choice('0123456789abcdef') for _ in range(10)])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.call(['ping', generate_random_hex()])
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}