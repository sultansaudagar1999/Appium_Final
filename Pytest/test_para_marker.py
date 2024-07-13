import pytest


def get_data():

    return [
        ("sultansaudagar1999@gmail.com","123456"),
        ("sultansaudagar2000@gmail.com", "123456"),
        ("sultansaudagar2001@gmail.com", "123456")
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username,"+++",password)