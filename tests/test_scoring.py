"""Test scoring functions."""
from src.scoring import score


def test_scoring():
    """Test scoring."""
    pattern = "ab.*"
    inlist = [
        "abbot",
        "absolute",
    ]
    outlist = [
        "rabbit",
        "alba",
    ]
    assert score(pattern, inlist, outlist) == {
        "true_positives": 2,
        "true_negatives": 2,
        "false_positives": 0,
        "false_negatives": 0,
        "accuracy": 1.0,
    }
    pattern = "ab.*"
    inlist = [
        "abbot",
        "rabbit",
    ]
    outlist = [
        "absolute",
        "alba",
    ]
    assert score(pattern, inlist, outlist) == {
        "true_positives": 1,
        "true_negatives": 1,
        "false_positives": 1,
        "false_negatives": 1,
        "accuracy": 0.5,
    }
