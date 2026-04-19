from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(True)
    notes: str | None = Field(max_length=200)


def main(space: SpaceStation) -> None:
    print(f"ID: {space.station_id}")
    print(f"Name: {space.name}")
    print(f"Crew: {space.crew_size} people")
    print(f"Power: {space.power_level}%")
    print(f"Oxygen: {space.oxygen_level}%")
    print(f"Status: "
          f"{'Operational' if space.is_operational else 'Not Operational'}")


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    try:
        Space = SpaceStation(
                    station_id="ISS001",
                    name="International Space Station",
                    crew_size=6,
                    power_level=85.5,
                    oxygen_level=92.3,
                    last_maintenance=datetime.now(),
                    is_operational=True, notes=None
                    )
    except ValidationError as e:
        print(e)
    main(Space)
    print("\n========================================")
    print("Expected validation error:")
    try:
        Space = SpaceStation(
                    station_id="ISS001",
                    name="International Space Station",
                    crew_size=22,
                    oxygen_level=85.5,
                    power_level=92.3,
                    last_maintenance=datetime.now(),
                    is_operational=True,
                    notes=None)
    except ValidationError as e:
        print(e.errors()[0]['msg'])
