import os
import tempfile

import pytest

from api import api


@pytest.fixture
def client():
    #db_fd, api.app.config['DATABASE'] = tempfile.mkstemp()

    api.app.config['TESTING'] = True

    with api.app.test_client() as client:
        # with api.app.app_context():
        #     api.init_db()
        yield client

    # os.close(db_fd)
    # os.unlink(api.app.config['DATABASE'])
