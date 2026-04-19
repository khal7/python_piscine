from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    number_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field('planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def rule_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("something")
        if (not any(m.rank in [Rank.commander, Rank.captain]
                    for m in self.crew)):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print("Mission: Mars Colony Establishment")
    try:
        sarah = CrewMember(
                    number_id="S1_00",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=20,
                    specialization="Mission Command",
                    years_experience=5,
                    is_active=True
                        )
        john = CrewMember(
                    number_id="S2_00",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=20,
                    specialization="Navigation",
                    years_experience=7,
                    is_active=True
                        )
        alice = CrewMember(
                    number_id="S3_00",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=20,
                    specialization="Engineering",
                    years_experience=9,
                    is_active=True
                        )
        crew_members = [sarah, john, alice]
        mission = SpaceMission(
                    mission_id="M2024_MARS",
                    mission_name="Mars Colony Establishment",
                    destination="Mars",
                    launch_date=datetime(2024, 6, 15, 22, 30, 0),
                    duration_days=900,
                    crew=crew_members,
                    mission_status='planned',
                    budget_millions=2500.0,
                            )
    except ValidationError as e:
        print(e)
    print(f"ID: {mission.mission_id}")
    print(f"Desitnation: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        bad_crew = [
            CrewMember(
                number_id="S1_00",
                name="Sarah Connor",
                rank=Rank.cadet, age=20,
                specialization="Mission Command",
                years_experience=5,
                is_active=True),
        ]
        SpaceMission(
                mission_id="M2024_MARS",
                mission_name="Mars Colony Establishment",
                destination="Mars",
                launch_date=datetime(2024, 6, 15, 22, 30, 0),
                duration_days=900,
                crew=bad_crew,
                mission_status='planned',
                budget_millions=2500.0)
    except ValidationError as e:
        for error in e.errors():
            print(error['ctx']['error'])
