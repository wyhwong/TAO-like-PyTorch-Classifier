from classifier_trains.core.model.utils import initialize_classifier
from classifier_trains.schemas.config import ModelConfig
from classifier_trains.schemas.constants import ModelBackbone


def model_config_factory(backbone: ModelBackbone) -> ModelConfig:
    """Return a model configuration object with the given backbone.

    Args:
        backbone (ModelBackbone): The backbone.

    Returns:
        ModelConfig: The model configuration.
    """

    return ModelConfig(backbone=backbone, num_classes=2, weights="DEFAULT")


def test_initialize_resnet() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.resnets():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.fc.out_features == 2


def test_initialize_alexnet() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.alexnets():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.classifier[6].out_features == 2


def test_initialize_vgg() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.vggs():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.classifier[6].out_features == 2


def test_initialize_squeezenet() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.squeezenets():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.classifier[1].out_channels == 2
        assert model.num_classes == 2


def test_initialize_densenet() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.densenets():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.classifier.out_features == 2


def test_initialize_inception() -> None:
    """Test the initialize classifier function"""

    for backbone in ModelBackbone.inceptionnets():
        model_config = model_config_factory(backbone)
        model = initialize_classifier(model_config)
        assert model.AuxLogits.fc.out_features == 2
        assert model.fc.out_features == 2
