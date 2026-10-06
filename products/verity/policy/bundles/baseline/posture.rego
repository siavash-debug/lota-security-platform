package posture

import future.keywords.contains
import future.keywords.if
import future.keywords.in

# Default decision sets
default allow := false

# Check for public administrative interface exposure
deny contains msg if {
    input.asset.type == "misp"
    input.controls.public_admin_exposure == true
    msg := "MISP administrative interface is publicly reachable."
}

# Check for missing MFA on privileged access
deny contains msg if {
    input.asset.type == "velociraptor"
    input.controls.mfa_required == false
    msg := "MFA is required for privileged Velociraptor access."
}

# Check for API keys exceeding maximum retention age (90 days)
warn contains msg if {
    input.controls.api_keys_over_90_days > 0
    msg := "One or more API keys exceed the maximum key age."
}

# Check for containers executing as root
deny contains msg if {
    input.container.run_as_root == true
    msg := "Container runs as root."
}

# Check for Docker socket mounted into container
deny contains msg if {
    input.container.docker_socket_mounted == true
    msg := "Container mounts the Docker socket."
}

# Allow evaluation if zero deny rules fired
allow if {
    count(deny) == 0
}
