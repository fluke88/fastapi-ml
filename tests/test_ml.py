import pytest

from ml.model import CostPrediction, load_staff


@pytest.fixture(scope="function")
def model():
    # Load the model once for each test function
    return load_staff()


@pytest.mark.parametrize(
    "params, expected_cost",
    [
        ([['2018-03-19', 56.9989, 70.48573, 1, 1, 1, 1, 20, 10, 1, 1, 'Санкт-Петербург']], 1018899.6190289664),
    ],
)
def test_param(model, params: list, expected_cost: str):
    model_pred = model(params)
    assert isinstance(model_pred, CostPrediction)
    assert model_pred.score == expected_cost
