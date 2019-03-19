import pytest
from Application.AppWiki import App


@pytest.fixture(scope="session")
def wikifixture():
    app = App()
    yield app
    app.destroy()



