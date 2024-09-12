import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

## url_webhook = "https://e87b-187-105-62-25.ngrok-free.app/"

@app.get("/")
async def root():
    return "Webhooks com FastAPI Python"

@app.post('/issue')
async def issue(request: Request):
     
     data = await request.json()
     
     with open('payload.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
     if data:
        print("Payload JSON:", data)
        return JSONResponse(content={"message": "Webhook recebido e salvo com sucesso!"}, status_code=200)

     else:
        return JSONResponse(content={"error": "Payload inválido"}, status_code=400)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)