# Home Assistant Configuration

This is my [Home Assistant](https://home-assistant.io) configuration. This also includes my [ESPHome](https://esphome.io) device configurations.

I plan to write up more about it at some point. [Follow me on Twitter](https://twitter.com/soffes) if you want to follow along.

## About my setup

### Installation

I run Home Assistant via [Hass.io](https://www.home-assistant.io/hassio/installation/) on my Synology NAS as a virtual machine. It works really well! (I was doing [plain Docker](https://www.home-assistant.io/docs/installation/docker/#synology-nas) at first.)

### HomeKit

I really like Apple's Home app and the Siri integration that comes with it. My wife also likes using the home app over something like the Home Assistant app.

My approach is to link everything directly to Home Assistant and then expose some devices to HomeKit from HomeAssistant. I do this with a whitelist so I can make sure everything in HomeKit is configured and will have a good experience in the Home app.

### Siri Shortcuts

I have a UniFi router and use it to configure a URL with Dynamic DNS for my house (and I’m not going to tell you what that is :P). I also exposed port forwarding for port `8123` to my Synology so I can reach Home Assistant externally.

Then you can follow this [simple guide](https://community.home-assistant.io/t/ios-shortcuts-with-ha-no-ssl-required/89529) to create a Siri Shortcut to do things. I made one that hits `/api/services/script/sonos_pause_all` so I can yell "Hey Siri, stop Sonos"! This is great for things you want to be able to control with Siri but don’t want to expose in the Home app.

### ZigBee

I use a [ConBee II](https://www.amazon.com/gp/product/B07PZ7ZHG5) with the [ZHA](http://home-assistant.io/integrations/zha/) integration to connect to my connect to my [ZigBee](https://en.wikipedia.org/wiki/ZigBee) devices. I’m currently only using this for [Aqara Door/Window Sensors](https://www.amazon.com/gp/product/B07D37VDM3) since the US version of their bridge isn’t scriptable.

## Questions?

Have questions about my setup? [Tweet me](https://twitter.com/soffes)!
