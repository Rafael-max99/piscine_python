#!/usr/bin/env python3

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):

    station_id: str = Field(
        ..., min_length=3, max_length=10, description="Station id")
    name: str = Field(
        ..., min_length=1, max_length=50, description="Station name")
    crew_size: int = Field(
        ..., ge=1, le=20, description="Number of crew members")
    power_level: float = Field(
        ..., ge=0.0, le=100.0, description="Power level percent")
    oxygen_level: float = Field(
        ..., ge=0.0, le=100.0, description="Oxygen level percent")
    last_maintenance: datetime = Field(
        ..., description="Last maintenance timestamp")
    is_operational: bool = Field(
        default=True, description="Operational status")
    notes: Optional[str] = Field(
        default=None, max_length=200, description="Additional notes")


def display_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Not Operational"
    print(f"Status: {status}")
    print(f"Last Maintenance: {station.last_maintenance}")
    if station.notes:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    # Valid
    print("Valid station created:")
    try:
        valid_station = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime.fromisoformat("2024-01-15T10:30:00"),
                is_operational=True,
                notes="Running smoothly"
        )
        display_station(valid_station)
    except Exception as e:
        print(f"Error: {e}")

    # Invalid
    print("\n" + "=" * 40)
    print("Expected validation error:")
    try:
        valid_station = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=25,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime.fromisoformat("2024-01-15T10:30:00")
        )
    except Exception as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    main()
