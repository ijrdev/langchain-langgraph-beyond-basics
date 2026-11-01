from typing import Literal, List

from pydantic import BaseModel, Field

class DestinationResearchResponse(BaseModel):
    """Informações do destino relevantes para o planejamento da viagem."""

    status: Literal["identified", "ambiguous", "unidentified"] = Field(description="Resultado obrigatório da pesquisa: 'identified' quando o destino foi identificado; 'ambiguous' quando houver mais de uma interpretação possível; ou 'unidentified' quando não for possível identificar ou pesquisar o destino.")
    destination: str | None = Field(description="Nome do destino identificado. Preencha se houver informação; caso contrário, retorne null.")
    city: str | None = Field(description="Cidade do destino, quando conhecida e aplicável. Preencha se houver informação; caso contrário, retorne null.")
    state: str | None = Field(description="Estado, província ou região do destino, quando conhecido e aplicável. Preencha se houver informação; caso contrário, retorne null.")
    country: str | None = Field(description="País do destino, quando conhecido. Preencha se houver informação; caso contrário, retorne null.")
    interest_information: List[str] | None = Field(description="Informações sobre os interesses do usuário no destino. Preencha se houver informações; caso contrário, retorne null.")
    restriction_information: List[str] | None = Field(description="Cuidados e informações relacionados às restrições do usuário no destino. Preencha se houver informações; caso contrário, retorne null.")
    practical_information: List[str] | None = Field(description="Informações práticas relevantes, como por exemplo: idioma, moeda e transporte. Preencha se houver informações; caso contrário, retorne null.")