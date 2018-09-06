from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.components.switch import PLATFORM_SCHEMA
from homeassistant.helpers.entity import ToggleEntity
import homeassistant.components.rpi_gpio as rpi_gpio
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import logging
import time

CONF_PORTS = 'ports'

DEPENDENCIES = ['rpi_gpio']

_LOGGER = logging.getLogger(__name__)

_SWITCHES_SCHEMA = vol.Schema({
	cv.positive_int: cv.string,
})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
	vol.Required(CONF_PORTS): _SWITCHES_SCHEMA
})


def setup_platform(hass, config, add_devices, discovery_info=None):
	switches = []
	ports = config.get(CONF_PORTS)

	for port, name in ports.items():
		switches.append(LatchingSwitch(name, port))

	add_devices(switches)

class LatchingSwitch(ToggleEntity):
	def __init__(self, name, port):
		self._name = name
		self._port = port
		self._state = False
		rpi_gpio.setup_output(self._port)
		rpi_gpio.write_output(self._port, 0)

	@property
	def name(self):
		return self._name

	@property
	def should_poll(self):
		return False

	@property
	def is_on(self):
		return self._state

	def turn_on(self, **kwargs):
		self.change_output(True)

	def turn_off(self, **kwargs):
		self.change_output(False)

	def change_output(self, newstate):
		if newstate != self._state:
			rpi_gpio.write_output(self._port, 1)
			time.sleep(.2)
			rpi_gpio.write_output(self._port, 0)
			self._state = not self._state
		self.schedule_update_ha_state()
