


def test_validate():
    exp_title = "Google"
    act_title = "Amazon"
    title = "Gmail"

    # if exp_title == act_title:
    #     print("Matching")
    # else:
    #     print("Not Matching")

    print("Begining")
    assert act_title == exp_title , "Titles Not Matching"
    assert "Gmail" in title, "Title matching"
    assert False , "Forcefully failed"
    print("Ending")
