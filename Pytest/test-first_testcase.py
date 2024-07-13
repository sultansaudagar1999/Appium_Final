import pytest
def setup_module(module):
    print("Start")

def teardown_module(module):
    print("End")

def setup_function(function):
    print("Launching Browser")

def teardown_funtion(function):
    print("Quitting Browser")


def test_login():
    print("Executed Succesfully")

def test_user_reg():
    print("Executed Succesfully")