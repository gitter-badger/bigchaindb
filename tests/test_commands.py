from argparse import Namespace

import pytest


@pytest.fixture
def mock_run_configure(monkeypatch):
    from bigchaindb.commands import bigchain
    monkeypatch.setattr(bigchain, 'run_configure', lambda *args, **kwargs: None)


@pytest.fixture
def mock_file_config(monkeypatch):
    from bigchaindb import config_utils
    monkeypatch.setattr(config_utils, 'file_config', lambda *args: None)


@pytest.fixture
def mock_db_init_with_existing_db(monkeypatch):
    from bigchaindb import db
    from bigchaindb.exceptions import DatabaseAlreadyExists

    def mockreturn():
        raise DatabaseAlreadyExists

    monkeypatch.setattr(db, 'init', mockreturn)


@pytest.fixture
def mock_processes_start(monkeypatch):
    from bigchaindb.processes import Processes
    monkeypatch.setattr(Processes, 'start', lambda *args: None)


def test_bigchain_run_start(mock_run_configure, mock_file_config,
                            mock_processes_start, mock_db_init_with_existing_db):
    from bigchaindb.commands.bigchain import run_start
    args = Namespace(config=None, yes=True)
    run_start(args)