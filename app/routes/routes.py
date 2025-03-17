from fastapi import APIRouter
from app.dto.extract_request_dto import ExtractRequestDTO

router = APIRouter()

@router.get("/")
def hello():
    return {"message": "Hello World"}

@router.post('/extract')
def extract_metadata(request: ExtractRequestDTO):
     return {
        "message": "Extração iniciada com sucesso",
        "extractMethod": request.extractMethod,
        "extractUrl": request.extractUrl,
        "extractFile": request.extractFile
    }
