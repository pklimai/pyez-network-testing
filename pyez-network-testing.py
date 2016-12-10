from __future__ import print_function
from jnpr.junos import Device
from os.path import split, splitext, isfile, join
from os import listdir

script_dir = split(__file__)[0] or "."
for f in listdir(script_dir):
    if isfile(join(script_dir, f)) and f.startswith("tests_") and f.endswith(".py"):
        exec("from %s import *" % splitext(f)[0])

HOSTS = {
    "R1": "10.254.0.35",
    "R2": "10.254.0.37",
    "R3": "10.254.0.38",
}

USER = "lab"
PASSWD = "lab123"

if __name__ == "__main__":

    tests_success = 0
    tests_fail = 0

    for host in sorted(HOSTS.keys()):
        print("Running tests for %s" % host)
        with Device(host=HOSTS[host], user=USER, passwd=PASSWD, gather_facts=False) as dev:
            for name in dir():
                if name.startswith("test_%s_" % host) or name.startswith("test_all_"):
                    print("    Running %s... " % name, end="")
                    test_result = locals()[name](dev)
                    if test_result:
                        print(" pass")
                        tests_success += 1
                    else:
                        print(" ***FAIL***")
                        tests_fail += 1

    print("--------")
    print("Network test script finished. Successful tests: %s, failed tests: %s" %
          (tests_success, tests_fail))
    print("All went OK." if tests_fail == 0 else "***WARNING***: There were failed tests!")

