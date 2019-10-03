import pytest
from WhPy import slack


def test_import():
    """
    Ensures slack module is imported
    """
    assert slack.Webhook, "Could not import slack.webhook"
