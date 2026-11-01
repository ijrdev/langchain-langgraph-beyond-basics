# from langgraph.graph.state import CompiledStateGraph

# from checkpoint_time_travel.workflows.trip_planning.graphs import TripPlanningWorkflow

# trip_planning_workflow: TripPlanningWorkflow = TripPlanningWorkflow()

# compiled_state_graph: CompiledStateGraph = trip_planning_workflow.build()

from pprint import pprint

from langgraph.graph.state import CompiledStateGraph

from checkpoint_time_travel.workflows.trip_planning.graphs import TripPlanningWorkflow

fake_inputs: list[dict] = [
    {
        "destination": "Florianópolis, Santa Catarina, Brasil",
        "duration_days": 5,
        "travelers": {
            "adults": 2,
            "children": 0,
            "babies": 0,
        },
        "budget": {
            "accommodation": 2500.0,
            "general_expenses": 1800.0,
            "transport": 800.0,
        },
        "interests": ["praias", "trilhas", "gastronomia"],
        "restrictions": ["evitar trilhas de alta dificuldade"],
    },
    {
        "destination": "Gramado, Rio Grande do Sul, Brasil",
        "duration_days": 4,
        "travelers": {
            "adults": 2,
            "children": 1,
            "babies": 0,
        },
        "budget": {
            "accommodation": 2000.0,
            "general_expenses": 1500.0,
            "transport": 600.0,
        },
        "interests": ["passeios em família", "gastronomia", "natureza"],
        "restrictions": ["atividades adequadas para crianças"],
    },
    {
        "destination": "Lisboa, Portugal",
        "duration_days": 7,
        "travelers": {
            "adults": 1,
            "children": 0,
            "babies": 0,
        },
        "budget": {
            "accommodation": 700.0,
            "general_expenses": 500.0,
            "transport": 150.0,
        },
        "interests": ["história", "museus", "gastronomia"],
        "restrictions": ["evitar atividades com muitas escadas"],
    },
]

trip_planning_workflow: TripPlanningWorkflow = TripPlanningWorkflow()
compiled_state_graph: CompiledStateGraph = trip_planning_workflow.build()

if __name__ == "__main__":
    test_input = fake_inputs[0]

    try:
        result = compiled_state_graph.invoke(test_input)
        
        pprint(result)
    except Exception as error:
        print(f"Erro durante o planejamento da viagem: {error}")