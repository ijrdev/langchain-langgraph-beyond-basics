from typing import Literal, List

from pydantic import BaseModel, Field

class Activity(BaseModel):
    name: str | None = Field(description="Nome da atividade, se disponível. Caso contrário, retorne null.")
    description: str | None = Field(description="Descrição da atividade e sua relação com os interesses dos viajantes. Caso contrário, retorne null.")
    location: str | None = Field(description="Local da atividade, se conhecido. Caso contrário, retorne null.")
    estimated_cost: float | None = Field(description="Custo estimado da atividade para o grupo, se houver informação disponível. Caso contrário, retorne null.")
    currency: str | None = Field(description="Moeda do custo informado, se conhecida. Caso contrário, retorne null.")
    transport_information: str | None = Field(description="Informações de deslocamento para a atividade, se disponíveis. Caso contrário, retorne null.")
    considerations: List[str] | None = Field(description="Cuidados ou limitações relevantes para os viajantes. Caso contrário, retorne null.")
    source: str | None = Field(description="URL ou referência da fonte efetivamente consultada. Caso contrário, retorne null.")

class ActivityDay(BaseModel):
    day: int = Field(description="Número do dia da viagem, começando em 1.")
    activities: List[Activity] | None = Field(description="Atividades propostas para o dia. Retorne null se não houver atividades disponíveis.")

class ActivityPlannerResponse(BaseModel):
    """Resultado do planejamento das atividades da viagem."""

    status: Literal["completed", "partial", "unavailable"] = Field(description="Resultado obrigatório do planejamento: 'completed' quando for possível apresentar uma programação para a viagem; 'partial' quando a programação tiver informações ou dias pendentes; ou 'unavailable' quando não for possível propor uma programação.")
    days: List[ActivityDay] | None = Field(description="Programação de atividades organizada por dia. Retorne null se não for possível montar a programação.")
    budget_considerations: List[str] | None = Field(description="Considerações sobre despesas gerais e transporte. Retorne null se não houver informações.")
    pending_information: List[str] | None = Field(description="Dados ausentes ou informações que precisam ser confirmadas. Retorne null se não houver pendências identificadas.")
