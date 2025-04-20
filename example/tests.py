testinfra_hosts = [
    "ssh://ubuntu2404",
    "ssh://debian12",
    "ssh://almalinux9",
    "ssh://fedora41"
]


def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled
