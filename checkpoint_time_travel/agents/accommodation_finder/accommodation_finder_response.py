from typing import Literal, List

from pydantic import BaseModel, Field

class AccommodationOption(BaseModel):
    name: str | None = Field(description="Nome da hospedagem, se conhecido. Caso contrário, retorne null.")
    location: str | None = Field(description="Localização da hospedagem, se conhecida. Caso contrário, retorne null.")
    description: str | None = Field(description="Descrição relevante da hospedagem para o grupo. Caso contrário, retorne null.")
    estimated_cost: float | None = Field(description="Custo estimado para a estadia, se houver informação disponível. Caso contrário, retorne null.")
    currency: str | None = Field(description="Moeda do custo informado, se conhecida. Caso contrário, retorne null.")
    considerations: List[str] | None = Field(description="Pontos relevantes sobre localização, viajantes ou restrições. Caso contrário, retorne null.")
    source: str | None = Field(description="URL ou referência da fonte efetivamente consultada. Caso contrário, retorne null.")

class AccommodationFinderResponse(BaseModel):
    """Resultado da pesquisa de hospedagens para a viagem."""

    status: Literal["completed", "partial", "unavailable"] = Field(description="Resultado obrigatório da pesquisa: 'completed' quando houver informações suficientes para apresentar opções; 'partial' quando houver opções com informações ou verificações pendentes; ou 'unavailable' quando não for possível apresentar opções.")
    options: List[AccommodationOption] | None = Field(description="Opções de hospedagem encontradas. Retorne null se nenhuma opção puder ser apresentada.")
