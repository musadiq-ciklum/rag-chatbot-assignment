import sys
import os
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


@pytest.fixture
def pdf_path():
    """Fixture: path to the reference PDF."""
    return "data/raw/slides/Databases_for_GenAI.pdf"


@pytest.fixture
def test_output_dir(tmp_path):
    """Fixture: create a temporary directory for test outputs."""
    return tmp_path
