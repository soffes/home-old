"""Config flow of our component"""

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME
)
from .const import DOMAIN


@config_entries.HANDLERS.register(DOMAIN)
class IoCareConfigFlow(config_entries.ConfigFlow):
    """Handle our config flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle a flow start."""

        fields = vol.Schema({
            vol.Required(CONF_USERNAME): str,
            vol.Required(CONF_PASSWORD): str
        })

        if user_input is not None:
            return self.async_create_entry(
                title="Coway IoCare Config Entry",
                data=user_input,
            )

        return self.async_show_form(step_id="user", data_schema=fields)
