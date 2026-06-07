#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(
        ..., min_length=3, max_length=10, description="Member id")
    name: str = Field(
        ..., min_length=2, max_length=50, description="Member name")
    rank: Rank = Field(
        ..., description="Member rank")
    age: int = Field(
        ..., ge=18, le=80, description="Member age in years")
    specialization: str = Field(
        ..., min_length=3, max_length=30, description="Member specialization")
    years_experience: int = Field(
        ..., ge=0, le=50, description="Member years of experience")
    is_active: bool = Field(
        default=True, description="Active status")


class SpaceMission(BaseModel):
    mission_id: str = Field(
        ..., min_length=5, max_length=15, description="Mission id")
    mission_name: str = Field(
        ..., min_length=3, max_length=100, description="Mission name")
    destination: str = Field(
        ..., min_length=3, max_length=50, description="Mission destination")
    launch_date: datetime = Field(
        ..., description="Launch date and time")
    duration_days: int = Field(
        ..., ge=1, le=3650,
        description="Mission duration in days (max 10 years)")
    crew: List[CrewMember] = Field(
        ..., min_length=1, max_length=12, description="Crew members (1-12)")
    mission_status: str = Field(
        default="planned", description="Mission status")
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0, description="Mission budget in millions")

    @model_validator(mode='after')
    def validate_safety_requirements(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank in [Rank.commander, Rank.captain]:
                has_leader = True
                break
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")

        experienced = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < len(self.crew) * 0.5:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


def display_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value})")
        print(f"    Specialization: {member.specialization}")
        print(f"    Experience: {member.years_experience} years")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    print("\nValid mission created:")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-06-01T14:30:00"),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True
                ),
                CrewMember(
                    member_id="002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        display_mission(valid_mission)
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "=" * 40)
    print("\nExpected validation error:")
    try:
        _ = SpaceMission(
            mission_id="M2024_VENUS",
            mission_name="Venus Research",
            destination="Venus",
            launch_date=datetime.fromisoformat("2024-07-01T10:00:00"),
            duration_days=180,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Jane Doe",
                    rank=Rank.officer,
                    age=28,
                    specialization="Science",
                    years_experience=3,
                    is_active=True
                )
            ],
            budget_millions=500.0
        )
    except Exception as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    main()
