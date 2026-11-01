from langgraph.graph import StateGraph, START, END

from checkpoint_time_travel.workflows.trip_planning.states import InputState, ExecutionState, OutputState
from checkpoint_time_travel.workflows.trip_planning.nodes import TripPlanningNodes

class TripPlanningWorkflow():
    def __init__(self):
        self.builder: StateGraph = StateGraph(ExecutionState, input_schema=InputState, output_schema=OutputState)
        self.trip_planning_nodes: TripPlanningNodes = TripPlanningNodes()
        
    def build(self):
        try:
            self.builder.add_node("destination_research_node", self.trip_planning_nodes.destination_research_node)
            self.builder.add_node("accommodation_finder_node", self.trip_planning_nodes.accommodation_finder_node)
            self.builder.add_node("activity_planner_node", self.trip_planning_nodes.activity_planner_node)
            self.builder.add_node("itinerary_compiler_node", self.trip_planning_nodes.itinerary_compiler_node)
            
            self.builder.add_edge(START, "destination_research_node")
            self.builder.add_edge("destination_research_node", "accommodation_finder_node")
            self.builder.add_edge("accommodation_finder_node", "activity_planner_node")
            self.builder.add_edge("activity_planner_node", "itinerary_compiler_node")
            self.builder.add_edge("itinerary_compiler_node", END)
            
            return self.builder.compile()
        except Exception:
            raise
            