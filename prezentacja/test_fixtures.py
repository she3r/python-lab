import pytest
# parametryzacja fixture
@pytest.fixture
def tester(tester_arg):
    """Create tester object"""
    return f"podany argument {tester_arg}"

@pytest.mark.parametrize('tester_arg',['TakiPodajeArgument'])
def test_fixture_params(tester):
    print(tester)
    assert tester == 'podany argument TakiPodajeArgument'
