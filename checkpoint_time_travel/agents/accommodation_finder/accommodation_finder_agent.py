import os

from deepagents.middleware.subagents import CompiledSubAgent
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.chat_models import init_chat_model

from checkpoint_time_travel.agents.accommodation_finder.accommodation_finder_response import AccommodationFinderResponse

class AccomodationFinderAgent():
    def __init__(self):
        self.name: str = "accommodation_finder_agent"
        self.description: str = "Busca opções de hospedagem adequadas ao destino, aos viajantes e ao orçamento."
        
        self.agent: CompiledStateGraph = create_agent(
            name=self.name,
            model=init_chat_model(
                model= f"{os.getenv('PROVIDER')}:{os.getenv('MODEL')}",
                api_key=os.getenv("API_KEY"),
                reasoning_effort=os.getenv("REASONING_EFFORT"),
            ),
            system_prompt="""
                Você é responsável pela etapa de hospedagem de uma viagem.

                Receba destiny_info, duration_days, travelers e budget.accommodation. Considere
                as características do destino, os interesses e as restrições registrados, a
                duração da viagem, a composição dos viajantes e o orçamento de hospedagem.
                Compare opções adequadas e apresente as informações relevantes para a escolha,
                incluindo localização, adequação ao grupo e custos quando disponíveis.

                Não invente estabelecimentos, preços, disponibilidade ou reservas. Não afirme
                ter pesquisado ou confirmado dados sem uma fonte confiável. Se faltarem datas,
                moeda ou outras informações necessárias, ou se não houver meios de verificar
                opções atuais, informe as limitações e apresente critérios de escolha em vez de
                tratar sugestões como opções confirmadas. Não monte o roteiro de atividades.

                Retorne somente um objeto JSON para accommodation_data, com opções verificadas
                quando disponíveis, critérios utilizados e eventuais incertezas ou pendências.
            """,
            response_format=AccommodationFinderResponse
        )
