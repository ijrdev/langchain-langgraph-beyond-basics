from typing import Literal

from pydantic import BaseModel, Field

class ItineraryCompilerResponse(BaseModel):
    """Resultado da revisão e apresentação do roteiro final."""

    status: Literal["completed", "partial", "unavailable"] = Field(description="Resultado obrigatório da montagem: 'completed' quando o roteiro puder ser apresentado com as informações disponíveis; 'partial' quando houver lacunas ou divergências relevantes; ou 'unavailable' quando não for possível montar o roteiro.")
    final_itinerary: str | None = Field(description="Roteiro final apresentado de forma clara ao usuário. Retorne null se não for possível montá-lo.")