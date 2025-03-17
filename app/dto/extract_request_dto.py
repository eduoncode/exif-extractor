from pydantic import BaseModel, Field, model_validator
from typing import Optional

class ExtractRequestDTO(BaseModel):
    extractMethod: str = Field(..., description="Método de extração obrigatório")
    extractUrl: Optional[str] = Field(None, description="URL do arquivo a ser extraído")
    extractFile: Optional[str] = Field(None, description="Nome do arquivo local a ser extraído")

    @model_validator(pre=True)
    def check_at_least_one(cls, values):
        if not values.get("extractUrl") and not values.get("extractFile"):
            raise ValueError("É necessário fornecer pelo menos um dos campos: extractUrl ou extractFile.")
        return values
