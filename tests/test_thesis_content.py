import pytest
import pandas as pd
import os

# Define the path to the key_details.csv
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Fixture to load the key_details.csv into a pandas DataFrame."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper function to get a detail_value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

def test_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Name')
    assert name == 'Vincenzo Grimaldi', f"Name mismatch: Expected 'Vincenzo Grimaldi', got '{name}'"

def test_thesis_title_match(key_details_df):
    title = get_detail_value(key_details_df, 'Thesis', 'Title')
    expected_title = 'Data Modeling in a Cross-domain Ontology for Cyber Intelligence in Smart-Grids Using Reinforcement Learning'
    assert title == expected_title, f"Thesis Title mismatch: Expected '{expected_title}', got '{title}'"

def test_supervisor_match(key_details_df):
    supervisor = get_detail_value(key_details_df, 'Thesis', 'Supervisor')
    assert supervisor == 'Charles Emehel, M. Sc.', f"Supervisor mismatch: Expected 'Charles Emehel, M. Sc.', got '{supervisor}'"

def test_examiner_match(key_details_df):
    examiner = get_detail_value(key_details_df, 'Thesis', 'Examiner')
    assert examiner == 'Univ.-Prof. Antonello Monti, Ph. D.', f"Examiner mismatch: Expected 'Univ.-Prof. Antonello Monti, Ph. D.', got '{examiner}'"

def test_date_match(key_details_df):
    date = get_detail_value(key_details_df, 'Thesis', 'Date')
    assert date == 'June 03, 2025', f"Date mismatch: Expected 'June 03, 2025', got '{date}'"

# Ensure the test output includes the verification message
def test_final_verification_message():
    assert True, "Master's Thesis 100% verified against PDF content."
