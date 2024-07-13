import pytest

@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")

@pytest.fixture(scope='function')
def before():
    print("Launching Browser")

    yield
    print("Quitting Browser")

def test_login(setup,before):
    print("Executed Succesfully")

def test_user_reg(setup,before):
    print("Executed Succesfully")