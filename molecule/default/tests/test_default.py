import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    # apt packages
    expected_packages = [
        'python-pip'
    ]
    for package in expected_packages:
        assert host.package(package).is_installed


def test_installed_pip_packages(host):
    # pip packages
    expected_pip_packages = [
        'boto'
    ]
    actual_pip_packages = host.pip_package.get_packages()

    for package in expected_pip_packages:
        assert package in actual_pip_packages
