# models.py
"""Pydantic models that define the schema used by the [bfrpg_monster_loader][bfrpg_monster_loader.bfrpg_monster_loader] module to load semi-structured monster data from `*.txt` files into a structured format that may be further processed by other tools."""  # noqa: E501

from typing import Optional
from pydantic import BaseModel, Field


class Attack(BaseModel):
    """One attack that may be made by a monster."""

    attack_type: str = Field(..., description="The source of the attack, like bite, claw, or weapon.")
    num_attacks: int = Field(
        ..., description="The number of attacks the monster can make per round with this attack type."
    )
    damage_die: str = Field(..., description="The die roll in XdY format to use when the monster hits an opponent.")


class Appearance(BaseModel):
    """Potential appearances for a monster in different contexts."""

    context: str = Field(..., description="The context in which the monster appears, like 'Lair' or 'Wild'.")
    die_roll: str = Field(
        ..., description="The die roll in XdY format used to determine the number of monsters appearing."
    )


class Movement(BaseModel):
    """Different types of movement available to a monster."""

    movement_type: str | None = Field(
        ..., description="The type of movement, like walking, flying, swimming (or None if no movement type is listed)."
    )
    rate: str = Field(..., description="The rate at which the monster can move in this movement type.")
    turning_distance: str | None = Field(..., description="The distance the monster can turn at this movement rate.")


class ArmorDetail(BaseModel):
    """Detail for an armor class setting."""

    description: str | None = Field(
        None, description="Description of the armor configuration like 'unarmored' or 'with shield'."
    )
    value: int = Field(..., description="The armor class value in this configuration.")


class Monster(BaseModel):
    name: str = Field(..., description="The name of the monster.")
    armor_classes: list[ArmorDetail] = Field(..., description="List of armor class configurations.")
    hit_dice: str = Field(..., description="The hit dice of the monster in XdY format.")
    attacks: list[Attack] = Field(..., description="List of attacks the monster can perform.")
    movement_rates: list[Movement] = Field(..., description="Movement types (e.g. fly, run, walk) and their rates.")
    appearances: list[Appearance] = Field(..., description="List of different appearances in various contexts.")
    save_as_class: str = Field(..., description="The class to use for saving throws.")
    save_as_level: int = Field(..., description="The level to use for saving throws")
    morale: str = Field(..., description="The morale of the monster.")
    treasure_type: str
    xp: int
    description: Optional[str] = None


class Bestiary(BaseModel):
    monsters: list[Monster]
