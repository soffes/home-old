import appdaemon.plugins.hass.hassapi as hass
import datetime

class Dim(hass.Hass):
    def initialize(self):
        self.timer = None
        self.run_at_sunrise(self.sunrise_cb)
        self.run_at_sunset(self.sunset_cb)
        self.start_timer()

    def sunrise_cb(self, kwargs):
        if self.timer is None:
            return

        self.cancel_timer(self.timer)

    def sunset_cb(self, kwargs):
        self.start_timer()

    def start_timer(self):
        self.timer = self.run_minutely(self.timer_cb, datetime.time(0, 0, 0))

    def timer_cb(self, kwargs):
        sunset = self.sunset()
        sunrise = self.sunrise()
        now = self.datetime()

        night_minutes = (sunrise - sunset).seconds / 60
        percent = (sunset - now).seconds / 60 / night_minutes / 2
        brightness = int((1 - percent) * 255)

        self.turn_on("light.sams_lamp", brightness = brightness)
        self.turn_on("light.ellens_lamp", brightness = brightness)
        self.turn_on("light.master_bedroom_overhead", brightness = brightness)
        self.turn_on("light.master_bedroom_hallway_overhead", brightness = brightness)
