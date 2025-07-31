import pytest

@pytest.mark.alpha  # Mark with label alpha
def test_one():
    assert 1

class TestStuff:
    # @pytest.mark.wombat
    @pytest.mark.alpha  # Mark with label alpha
    def test_two(self):
        assert 1

    @pytest.mark.beta  # Mark with label beta
    @pytest.mark.gamma
    def test_three(self ):
        assert 1

