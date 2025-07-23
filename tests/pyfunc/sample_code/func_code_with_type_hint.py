import typing

from mlflow.models import set_model


def predict(model_input: typing.List[str]):
    return model_input


set_model(predict)
