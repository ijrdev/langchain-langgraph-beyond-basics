from pydantic import BaseModel

class TravelersModel(BaseModel):
    adults: int = 0
    children: int = 0
    babies: int = 0

class BudgetModel(BaseModel):
    accommodation: float = 0
    general_expenses: float = 0
    transport: float = 0

class InputState(BaseModel):
    destination: str = ""
    duration_days: int = 0
    travelers: TravelersModel
    budget: BudgetModel
    interests: list = []
    restrictions: list = []

class ExecutionState(InputState):
    destiny_info: dict | None = None
    accommodation_data: dict | None = None
    activities_data: dict | None = None
    final_itinerary: str | None = None

class OutputState(BaseModel):
    final_itinerary: str | None = None