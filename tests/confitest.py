# Generated by [Toolkit-Py](https://github.com/fujiawei-dev/toolkit-py) Generator
# Created at 2022-02-06 10:58:35.566935, Version 0.2.9

def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 5:
        session.exitstatus = 0
