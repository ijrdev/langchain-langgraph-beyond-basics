import os

from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.chat_models import init_chat_model

from checkpoint_time_travel.agents.destination_research.destination_research_response import DestinationResearchResponse   

class DestinationResearchAgent():
    """Valida o destino e reúne informações úteis para o planejamento da viagem."""
    
    def __init__(self):
        self.agent: CompiledStateGraph = create_agent(
            name="destination_research_agent",
            model=init_chat_model(
                model= f"{os.getenv('PROVIDER')}:{os.getenv('MODEL')}",
                api_key=os.getenv("API_KEY"),
                reasoning_effort=os.getenv("REASONING_EFFORT"),
            ),
            system_prompt="""
                Você é responsável pela etapa de pesquisa do destino de uma viagem.

                Receba destination, interests e restrictions. Identifique o destino e verifique
                se as informações fornecidas são suficientes para identificá-lo. Considere os
                interesses e as restrições ao reunir informações relevantes para as próximas
                etapas, como localização, características gerais e cuidados importantes.

                Não invente fatos nem afirme ter confirmado informações sem uma fonte confiável.
                Se o destino for ambíguo, os dados forem insuficientes ou não for possível
                verificá-los, explique a limitação e indique o que precisa ser esclarecido.
                Não escolha hospedagens nem monte o roteiro de atividades.

                Retorne somente um objeto JSON para destiny_info, com destino identificado,
                informações relevantes, interesses e restrições considerados, além de eventuais
                incertezas ou informações pendentes.
            """,
            response_format=DestinationResearchResponse
        )
