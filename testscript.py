import os
import logging

from hyundai_kia_connect_api.VehicleManager import VehicleManager


def test_CA_login():
    username = "jmdirk@gmail.com"
    password = "C3nt3rl1n3!"
    pin = "2015"
    vm = VehicleManager(
        region=2,
        brand=3,
        username=username,
        password=password,
        pin=pin,
        geocode_api_enable=True,
    )
    vm.check_and_refresh_token()
    vm.check_and_force_update_vehicles(force_refresh_interval=600)
    assert len(vm.vehicles.keys()) > 0

logging.basicConfig(level=logging.DEBUG)
test_CA_login()
