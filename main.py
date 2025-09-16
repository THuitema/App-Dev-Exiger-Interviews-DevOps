"""
To run:
1. `pip install -r requirements.txt`
1. `fastapi dev main.py`
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/', status_code=200)
def helloWorld():
    return {'message': 'Hello World!'}