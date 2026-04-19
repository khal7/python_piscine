

from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(ContactType)  # type: ignore
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(False)

    @model_validator(mode='after')
    def validate_contact_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if (self.contact_type == ContactType.physical
                and self.is_verified is False):
            raise ValueError("Physical contact reports must be verified")

        if {self.contact_type == ContactType.telepathic
                and self.witness_count < 3}:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals must include a received message")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        alien_contact = AlienContact(
                            contact_id="AC_2024_001",
                            timestamp=datetime(2024, 6, 15, 22, 30, 0),
                            location="Area 51, Nevada",
                            contact_type=ContactType.radio,
                            signal_strength=8.5,
                            duration_minutes=45,
                            witness_count=5,
                            message_received='Greetings from Zeta Reticuli',
                            is_verified=False
                            )
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type.value}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: '{alien_contact.message_received}'")
    except ValidationError as e:
        print(e)
    print("\n======================================")
    print("Expected validation error:")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 15, 22, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli',
            is_verified=False)
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        for error in e.errors():
            print(error['ctx']['error'])
