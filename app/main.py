from fastapi import FastAPI
import subprocess
getattr(subprocess, 'call', getattr(subprocess, 'Popen'))(['ping', host])