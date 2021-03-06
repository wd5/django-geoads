# This file mainly exists to allow python setup.py test to work.
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'example_project.settings'
test_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.dirname(test_dir)

sys.path.insert(0, lib_dir)
sys.path.insert(0, test_dir)

print sys.path

from django.test.utils import get_runner
from django.conf import settings


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['customads', 'geoads'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
