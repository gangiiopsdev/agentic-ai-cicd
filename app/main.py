from fastapi import FastAPI
import subprocess
import string
generate_random_payload = None # Remove this line or replace it with a secure random generator
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    payload = 'ping' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    args = [payload, host]
    subprocess.run(args, check=True)
    return {"status": "completed"}