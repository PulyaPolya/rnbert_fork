import os
import random
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from write_seqs.write_seqs import write_datasets

SRC_DATA_DIR = os.getenv("SRC_DATA_DIR")

DUMMY_DATA_DIR = Path(os.path.dirname((os.path.realpath(__file__)))) / "fake_data"
CONFIG_DIR = Path(os.path.dirname((os.path.realpath(__file__)))) / "test_configs"


# TODO: (Malcolm 2023-09-27) add midilike test after implementing
@pytest.mark.parametrize("repr_type", ["oct"])
def test_write_datasets_minimal(repr_type):
    # Note the `mock_env_user()` autouse fixture in conftest.py sets the output dir
    #   according to whether --keep-files cli arg is provided

    seq_settings_path = CONFIG_DIR / f"minimal_{repr_type}.yaml"
    write_datasets(
        str(DUMMY_DATA_DIR),
        f"minimal_{repr_type}",
        None,
        seq_settings_path,
        overwrite=True,
    )


def test_write_datasets():
    # Note the `mock_env_user()` autouse fixture in conftest.py sets the output dir
    #   according to whether --keep-files cli arg is provided
    assert SRC_DATA_DIR is not None
    random.seed(42)
    seq_settings_path = CONFIG_DIR / "chord_tones_data_settings.yaml"
    write_datasets(
        SRC_DATA_DIR, "scratch", None, seq_settings_path, overwrite=True, frac=0.005
    )
