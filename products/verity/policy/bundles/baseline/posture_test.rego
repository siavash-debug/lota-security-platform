package posture_test

import future.keywords.if
import data.posture

test_misp_public_exposure_denied if {
    input := {
        "asset": {"id": "asset_01", "type": "misp"},
        "controls": {"public_admin_exposure": true, "mfa_required": true, "api_keys_over_90_days": 0},
        "container": {"run_as_root": false, "docker_socket_mounted": false}
    }
    count(posture.deny) == 1 with input as input
    posture.deny["MISP administrative interface is publicly reachable."] with input as input
}

test_velociraptor_missing_mfa_denied if {
    input := {
        "asset": {"id": "asset_02", "type": "velociraptor"},
        "controls": {"public_admin_exposure": false, "mfa_required": false, "api_keys_over_90_days": 0},
        "container": {"run_as_root": false, "docker_socket_mounted": false}
    }
    count(posture.deny) == 1 with input as input
    posture.deny["MFA is required for privileged Velociraptor access."] with input as input
}

test_container_run_as_root_denied if {
    input := {
        "asset": {"id": "asset_03", "type": "container"},
        "controls": {"public_admin_exposure": false, "mfa_required": true, "api_keys_over_90_days": 0},
        "container": {"run_as_root": true, "docker_socket_mounted": false}
    }
    count(posture.deny) == 1 with input as input
    posture.deny["Container runs as root."] with input as input
}

test_container_docker_socket_denied if {
    input := {
        "asset": {"id": "asset_04", "type": "container"},
        "controls": {"public_admin_exposure": false, "mfa_required": true, "api_keys_over_90_days": 0},
        "container": {"run_as_root": false, "docker_socket_mounted": true}
    }
    count(posture.deny) == 1 with input as input
    posture.deny["Container mounts the Docker socket."] with input as input
}

test_api_key_age_warning if {
    input := {
        "asset": {"id": "asset_05", "type": "generic"},
        "controls": {"public_admin_exposure": false, "mfa_required": true, "api_keys_over_90_days": 2},
        "container": {"run_as_root": false, "docker_socket_mounted": false}
    }
    count(posture.warn) == 1 with input as input
    posture.warn["One or more API keys exceed the maximum key age."] with input as input
}

test_fully_compliant_input_allowed if {
    input := {
        "asset": {"id": "asset_06", "type": "misp"},
        "controls": {"public_admin_exposure": false, "mfa_required": true, "api_keys_over_90_days": 0},
        "container": {"run_as_root": false, "docker_socket_mounted": false}
    }
    count(posture.deny) == 0 with input as input
    count(posture.warn) == 0 with input as input
    posture.allow with input as input
}
