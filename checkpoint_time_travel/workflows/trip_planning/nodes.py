import json

from checkpoint_time_travel.workflows.trip_planning.states import ExecutionState
from checkpoint_time_travel.agents.accommodation_finder.accommodation_finder_agent import AccomodationFinderAgent
from checkpoint_time_travel.agents.activity_planner.activity_planner_agent import ActivityPlannerAgent
from checkpoint_time_travel.agents.destination_research.destination_research_agent import DestinationResearchAgent
from checkpoint_time_travel.agents.itinerary_compiler.itinerary_compiler_agent import ItineraryCompilerAgent

class TripPlanningNodes():
    def __init__(self):
        self.accommodation_finder_agent: AccomodationFinderAgent = AccomodationFinderAgent()
        self.activity_planner_agent: ActivityPlannerAgent = ActivityPlannerAgent()
        self.destination_research_agent: DestinationResearchAgent = DestinationResearchAgent()
        self.itinerary_compiler_agent: ItineraryCompilerAgent = ItineraryCompilerAgent()
        
    def destination_research_node(self, state: ExecutionState) -> dict:
        try:
            agent_input: dict = {
                "destination": state.destination,
                "interests": state.interests,
                "restrictions": state.restrictions,
            }

            response: dict = self.destination_research_agent.agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": json.dumps(agent_input, ensure_ascii=False),
                        }
                    ]
                }
            )

            destination_data: dict = response["structured_response"].model_dump()

            if not destination_data.get("status") or destination_data["status"] == "unidentified":
                raise ValueError("Não foi possível identificar o destino da viagem.")

            return {"destiny_info": destination_data}
        except Exception:
            raise
    
    def accommodation_finder_node(self, state: ExecutionState) -> dict:
        try:
            agent_input: dict = {
                "destiny_info": state.destiny_info,
                "duration_days": state.duration_days,
                "travelers": state.travelers.model_dump(),
                "budget": {"accommodation": state.budget.accommodation}
            }

            response: dict = self.accommodation_finder_agent.agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": json.dumps(agent_input, ensure_ascii=False),
                        }
                    ]
                }
            )

            accommodation_data: dict = response["structured_response"].model_dump()

            if not accommodation_data.get("status") or accommodation_data["status"] == "unavailable":
                raise ValueError("Não foi possível encontrar opções de hospedagem.")

            return {"accommodation_data": accommodation_data}
        except Exception:
            raise

    def activity_planner_node(self, state: ExecutionState) -> dict:
        try:
            agent_input: dict = {
                "destiny_info": state.destiny_info,
                "accommodation_data": state.accommodation_data,
                "duration_days": state.duration_days,
                "travelers": state.travelers.model_dump(),
                "budget": {
                    "general_expenses": state.budget.general_expenses,
                    "transport": state.budget.transport,
                },
            }

            response: dict = self.activity_planner_agent.agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": json.dumps(agent_input, ensure_ascii=False),
                        }
                    ]
                }
            )

            activities_data: dict = response["structured_response"].model_dump()

            if not activities_data.get("status") or activities_data["status"] == "unavailable":
                raise ValueError("Não foi possível planejar as atividades da viagem.")

            return {"activities_data": activities_data}
        except Exception:
            raise

    def itinerary_compiler_node(self, state: ExecutionState) -> dict:
        try:
            agent_input: dict = {
                "destiny_info": state.destiny_info,
                "accommodation_data": state.accommodation_data,
                "activities_data": state.activities_data,
            }

            response: dict = self.itinerary_compiler_agent.agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": json.dumps(agent_input, ensure_ascii=False),
                        }
                    ]
                }
            )

            itinerary_data: dict = response["structured_response"].model_dump()

            if not itinerary_data.get("status") or itinerary_data["status"] == "unavailable":
                raise ValueError("Não foi possível montar o roteiro final da viagem.")

            return {"final_itinerary": itinerary_data["final_itinerary"]}
        except Exception:
            raise
