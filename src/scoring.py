"""Scoring."""
import re
from typing import Iterable

from pydantic import BaseModel


class Score(BaseModel):
    true_positives: int
    true_negatives: int
    false_positives: int
    false_negatives: int
    accuracy: float


def score(
        pattern: str,
        inlist: Iterable = tuple(),
        outlist: Iterable = tuple(),
) -> Score:
    """Score the pattern with respect to an inlist and outlist."""
    inresults = [
        re.fullmatch(pattern, instring) is not None for instring in inlist
    ]
    outresults = [
        re.fullmatch(pattern, outstring) is None for outstring in outlist
    ]
    true_positives = sum(inresults)
    false_negatives = len(inresults) - true_positives
    true_negatives = sum(outresults)
    false_positives = len(outresults) - true_negatives
    total = len(inresults) + len(outresults)
    return Score(
        **{
        "true_positives": true_positives,
        "true_negatives": true_negatives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "accuracy": (true_positives + true_negatives) / total,
        }
    )
