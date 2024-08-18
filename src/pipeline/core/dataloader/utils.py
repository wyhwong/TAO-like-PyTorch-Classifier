from typing import Optional

import lightning as pl
import torchvision
import torchvision.datasets as datasets

from pipeline.schemas.config import DataloaderConfig
from pipeline.schemas.constants import Phase


def get_datamodule_for_training(
    dataloader_config: DataloaderConfig,
    transforms: Optional[dict[Phase, torchvision.transforms.Compose]] = None,
) -> pl.LightningDataModule:
    """Get the datamodule from the dataloader configuration.

    Args:
        dataloader_config (DataloaderConfig): The dataloader configuration.
        transforms (Optional[dict[Phase, torchvision.transforms.Compose]], optional):
            The transforms. Defaults to None.

    Returns:
        pl.LightningDataModule: The datamodule.
    """

    if not transforms:
        transforms = {phase: None for phase in Phase}

    train_dataset = datasets.ImageFolder(
        root=dataloader_config.trainset_dir,
        transform=transforms[Phase.TRAINING],
    )
    val_dataset = datasets.ImageFolder(
        root=dataloader_config.valset_dir,
        transform=transforms[Phase.VALIDATION],
    )

    if dataloader_config.testset_dir:
        test_dataset = datasets.ImageFolder(
            root=dataloader_config.testset_dir,
            transform=transforms[Phase.VALIDATION],
        )
    else:
        test_dataset = None

    return pl.LightningDataModule.from_datasets(
        train_dataset=train_dataset,
        val_dataset=val_dataset,
        test_dataset=test_dataset,
        batch_size=dataloader_config.batch_size,
        num_workers=dataloader_config.num_workers,
    )