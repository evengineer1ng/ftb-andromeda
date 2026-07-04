"""Starfield re-theme of FTB's manufacturer heritage system.

Fills the gap left by the missing `plugins.ftb_heritage_templates` module (see
docs/DECISIONS.md, 2026-07-04 entry) — `ftb_game.py`'s `_generate_manufacturers_and_parts`
imports `HERITAGE_TEMPLATES` and `get_weighted_template(rng, tier)` from that module path;
this file provides the same names, themed for Settled Systems rover/ship component
manufacturers instead of real-world motorsport nationalities.

DRAFT: these are invented archetypes (not lifted from any specific in-lore Starfield
corporation) evoking UC-corporate / Freestar-frontier / outlaw-salvage / high-tech /
deep-frontier flavors. Soft sponsor ties to actual Starfield factions (UC, Freestar,
Ryujin, Stroud-Eklund, Crimson Fleet) are a separate, later layer (sponsorship, not
manufacturer identity) — see docs/ARCHITECTURE.md's "soft, non-hard-locked" design goal.
Rename/adjust freely; nothing here is meant to be final.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class HeritageTemplate:
    nationality: str  # repurposed as faction/regional flavor tag, not a real-world nationality
    naming_grammar: Dict[str, List[str]]  # keys: patterns, prefixes, suffixes
    philosophy_bias_stats: Dict[str, float] = field(default_factory=dict)  # subset of STATS_SCHEMAS['Manufacturer']
    tier_weights: Dict[int, float] = field(default_factory=lambda: {t: 1.0 for t in range(1, 6)})


HERITAGE_TEMPLATES: List[HeritageTemplate] = [
    HeritageTemplate(
        nationality="United Colonies",
        naming_grammar={
            "patterns": ["formal", "compound"],
            "prefixes": ["Colonial", "Atlantis", "Vanguard", "UC"],
            "suffixes": ["Dynamics", "Systems", "Industries", "Standard"],
        },
        philosophy_bias_stats={
            "build_quality": 12.0, "financial_stability": 15.0, "reliability_philosophy": 10.0,
            "risk_appetite": -15.0, "regulatory_adaptability": 12.0, "customer_support": 8.0,
        },
        tier_weights={1: 0.6, 2: 1.0, 3: 1.2, 4: 1.2, 5: 1.0},
    ),
    HeritageTemplate(
        nationality="Freestar Frontier",
        naming_grammar={
            "patterns": ["bold", "compound"],
            "prefixes": ["Akila", "Frontier", "Rustline", "Homestead"],
            "suffixes": ["Works", "Rigging", "Motors", "Outfitters"],
        },
        philosophy_bias_stats={
            "reliability_philosophy": 12.0, "risk_appetite": 10.0, "build_quality": -8.0,
            "financial_stability": -10.0, "development_cycle_speed": 8.0, "customer_support": 10.0,
        },
        tier_weights={1: 1.2, 2: 1.2, 3: 0.9, 4: 0.6, 5: 0.3},
    ),
    HeritageTemplate(
        nationality="Crimson Salvage",
        naming_grammar={
            "patterns": ["bold", "surname"],
            "prefixes": ["Blackflag", "Scrap", "Nomad", "Redline"],
            "suffixes": ["Salvage", "Retrofit", "Rigs", "Cartel"],
        },
        philosophy_bias_stats={
            "development_cycle_speed": 18.0, "risk_appetite": 20.0, "customer_support": -18.0,
            "financial_stability": -12.0, "quality_control_rigor": -12.0, "market_sensitivity": 10.0,
        },
        tier_weights={1: 1.3, 2: 1.0, 3: 0.7, 4: 0.4, 5: 0.2},
    ),
    HeritageTemplate(
        nationality="Ryujin Precision",
        naming_grammar={
            "patterns": ["modern", "tech"],
            "prefixes": ["Neon", "Zenith", "Quantum", "Meridian"],
            "suffixes": ["Precision", "Tech", "Labs", "Dynamics"],
        },
        philosophy_bias_stats={
            "cfd_capability": 15.0, "material_science_depth": 15.0, "innovation_rate": 12.0,
            "wind_tunnel_access": 12.0, "risk_appetite": -8.0, "brand_prestige": 10.0,
        },
        tier_weights={1: 0.3, 2: 0.6, 3: 1.0, 4: 1.3, 5: 1.4},
    ),
    HeritageTemplate(
        nationality="Deep Frontier Independent",
        naming_grammar={
            "patterns": ["compound", "elegant"],
            "prefixes": ["Halcyon", "Driftward", "Outland", "Nova"],
            "suffixes": ["Collective", "Fabrication", "Foundry", "Concern"],
        },
        philosophy_bias_stats={
            "innovation_rate": 15.0, "financial_stability": -15.0, "racing_pedigree": -10.0,
            "technical_heritage": -10.0, "development_cycle_speed": 10.0, "market_sensitivity": 8.0,
        },
        tier_weights={1: 1.0, 2: 1.1, 3: 1.0, 4: 0.8, 5: 0.5},
    ),
]


def get_weighted_template(rng, tier: int = 3) -> HeritageTemplate:
    """Weighted-random template pick for the given tier (1=lowest, 5=highest prestige)."""
    weights = [t.tier_weights.get(tier, 1.0) for t in HERITAGE_TEMPLATES]
    return rng.choices(HERITAGE_TEMPLATES, weights=weights, k=1)[0]
