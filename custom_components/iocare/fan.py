"""Support for Coway Air Purifiers."""

import logging

from homeassistant.components.fan import (
    FanEntity,
    SUPPORT_SET_SPEED,
    SPEED_OFF,
    SPEED_LOW,
    SPEED_MEDIUM,
    SPEED_HIGH,
)

from .const import (
    DOMAIN,
    IOCARE_FAN_OFF,
    IOCARE_FAN_LOW,
    IOCARE_FAN_MEDIUM,
    IOCARE_FAN_HIGH
)

SUPPORTED_SPEEDS = [SPEED_LOW, SPEED_MEDIUM, SPEED_HIGH]
SUPPORTED_FEATURES = SUPPORT_SET_SPEED

IOCARE_FAN_SPEED_TO_HASS = {
    IOCARE_FAN_OFF: SPEED_OFF,
    IOCARE_FAN_LOW: SPEED_LOW,
    IOCARE_FAN_MEDIUM: SPEED_MEDIUM,
    IOCARE_FAN_HIGH: SPEED_HIGH,
}

HASS_FAN_SPEED_TO_IOCARE = {v: k for (k, v) in IOCARE_FAN_SPEED_TO_HASS.items()}


_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Platform uses config entry setup."""
    pass


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Coway Air Purifier devices."""
    iocare = hass.data[DOMAIN]

    devices = []

    for device in iocare.devices():
        devices.append(AirPurifier(device))

    async_add_entities(devices)


class AirPurifier(FanEntity):
    """Representation of a Coway Airmega air purifier."""

    def __init__(self, device):
        self._device = device
        self._available = True

    @property
    def unique_id(self):
        """Return the ID of this purifier."""
        return self._device.device_id

    @property
    def name(self):
        """Return the name of the purifier if any."""
        return self._device.name

    @property
    def is_on(self):
        """Return true if the purifier is on"""
        return self._device.is_on

    @property
    def available(self):
        """Return true if switch is available."""
        return self._available

    @property
    def speed(self) -> str:
        """Return the current speed."""
        if not self.is_on:
            return SPEED_OFF
        return IOCARE_FAN_SPEED_TO_HASS.get(self._device.fan_speed)

    @property
    def speed_list(self) -> list:
        """Get the list of available speeds."""
        return SUPPORTED_SPEEDS

    @property
    def supported_features(self) -> int:
        """Flag supported features."""
        return SUPPORTED_FEATURES

    def turn_on(self, speed: str = None, **kwargs) -> None:
        """Turn the air purifier on."""
        self._device.set_power(True)
        if speed is not None:
            self.set_speed(speed)

    def turn_off(self, **kwargs) -> None:
        """Turn the air purifier off."""
        self._device.set_power(False)

    def set_speed(self, speed: str) -> None:
        """Set the fan_mode of the air purifier."""
        if speed == SPEED_OFF:
            return self.turn_off()
        self._device.set_fan_speed(HASS_FAN_SPEED_TO_IOCARE.get(speed))

    def update(self):
        """Update automation state."""
        _LOGGER.info("Refreshing device state")
        self._device.refresh()
