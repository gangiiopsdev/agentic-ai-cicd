from fastapi import FastAPI
class SafePing:
    @staticmethod
def safe_ping(host: str) -> None:
        args = ['ping', host]
        try:
            subprocess.run(args, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e.stderr.strip()}')

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {'status': 'completed'}