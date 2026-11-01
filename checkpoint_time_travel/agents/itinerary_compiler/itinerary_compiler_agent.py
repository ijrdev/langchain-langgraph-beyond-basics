import os

from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.chat_models import init_chat_model

from checkpoint_time_travel.agents.itinerary_compiler.itinerary_compiler_response import ItineraryCompilerResponse

class ItineraryCompilerAgent():
    def __init__(self):
        self.name: str = "itinerary_compiler_agent"
        self.description: str = "Revisa e reúne as informações da viagem em um roteiro final para o usuário."

        self.agent: CompiledStateGraph = create_agent(
            name=self.name,
            model=init_chat_model(
                model= f"{os.getenv('PROVIDER')}:{os.getenv('MODEL')}",
                api_key=os.getenv("API_KEY"),
                reasoning_effort=os.getenv("REASONING_EFFORT"),
            ),
            system_prompt="""
                Você é responsável por revisar e apresentar o roteiro final de uma viagem.

                Receba destiny_info, accommodation_data e activities_data. Reúna as informações
                em uma apresentação clara para o usuário, incluindo destino, hospedagem,
                programação por dia e considerações de transporte e orçamento quando disponíveis.
                Verifique a coerência entre as etapas e destaque informações ausentes,
                divergências, estimativas e pontos que ainda precisem de confirmação.

                Não invente dados, não resolva divergências por suposição e não apresente
                reservas, preços, disponibilidade ou informações não verificadas como confirmados.
                Se algo impedir uma conclusão confiável, explique isso no roteiro.

                Retorne somente o texto do roteiro final para final_itinerary.
            """,
            response_format=ItineraryCompilerResponse
        )
