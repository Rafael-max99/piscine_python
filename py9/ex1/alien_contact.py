#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        ..., min_length=5, max_length=15, description="Contact identifier")
    timestamp: datetime = Field(
        ..., description="Contact timestamp")
    location: str = Field(
        ..., min_length=3, max_length=100, description="Contact location")
    contact_type: ContactType = Field(
        ..., description="Type of contact")
    signal_strength: float = Field(
        ..., ge=0.0, le=10.0, description="Signal strength 0-10")
    duration_minutes: int = Field(
        ..., ge=1, le=1440, description="Duration in minutes (max 24h)")
    witness_count: int = Field(
        ..., ge=1, le=100, description="Number of witnesses")
    message_received: Optional[str] = Field(
        default=None, max_length=500, description="Received message")
    is_verified: bool = Field(
        default=False, description="Verification status")

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include received message")

        return self


def display_contact(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")
    print(f"Verified: {'Yes' if contact.is_verified else 'No'} ")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Valid
    print("\nValid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2024-01-15T10:30:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
            )
        display_contact(valid_contact)
    except Exception as e:
        print(f"Error: {e}")

    # Invalid
    print("\n" + "=" * 40)
    print("\nExpected validation error:")
    try:
        _ = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.fromisoformat("2024-01-15T11:00:00"),
            location="Nevada Desert",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,
            is_verified=False
            )
    except Exception as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    main()
