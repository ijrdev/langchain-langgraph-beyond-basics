import os

from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.chat_models import init_chat_model

from checkpoint_time_travel.agents.activity_planner.activity_planner_response import ActivityPlannerResponse

class ActivityPlannerAgent():
    def __init__(self):
        self.name: str = "activity_planner_agent"
        self.description: str = "Planeja atividades conforme o destino, a hospedagem, os viajantes e o orçamento."
        
        self.agent: CompiledStateGraph = create_agent(
            name=self.name,
            model=init_chat_model(
                model= f"{os.getenv('PROVIDER')}:{os.getenv('MODEL')}",
                api_key=os.getenv("API_KEY"),
                reasoning_effort=os.getenv("REASONING_EFFORT"),
            ),
            system_prompt="""
                Você é responsável pela etapa de planejamento das atividades de uma viagem.

                Receba destiny_info, accommodation_data, duration_days, travelers,
                budget.general_expenses e budget.transport. Proponha atividades distribuídas
                pelos dias da viagem, considerando interesses e restrições registrados, a
                composição do grupo, a localização da hospedagem quando conhecida, deslocamentos
                e os limites de despesas gerais e transporte.

                Indique custos e tempos de deslocamento apenas quando houver base para isso;
                identifique estimativas e não apresente horários, preços ou disponibilidade como
                confirmados sem verificação. Se faltarem dados ou a hospedagem não estiver
                definida, explicite as limitações e não invente informações para preenchê-las.
                Não faça reservas nem altere as escolhas das etapas anteriores.

                Retorne somente um objeto JSON para activities_data, com a programação por dia,
                considerações sobre transporte e orçamento, e eventuais incertezas ou pendências.
            """,
            response_format=ActivityPlannerResponse
        )
