from dataclasses import dataclass


@dataclass
class Lipid:
    name: str | None = None
    owner_id: int | None = None
    alternative_name: str | None = None
    molecular_formula: str | None = None
    molecular_weight: str | None = None
    cas_number: str | None = None
    stock_solution_prep: str | None = None
    solubility: str | None = None
    conditions_for_use: str | None = None
    conditions_for_storage: str | None = None
    safety_information: str | None = None
    impurities: str | None = None
    source: str | None = None
    description: str | None = None
