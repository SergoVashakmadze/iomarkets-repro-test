# Deliberately failing: checks that a red CI run on a race's pull request gets the App's send-back comment. Removed right after.
def test_sendback_probe():
    assert False, "deliberate failure for the send-back test"
# retrigger
