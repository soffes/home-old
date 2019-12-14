# Home Assistant Configuration

This is my [Home Assistant](https://home-assistant.io) configuration. This also includes my [ESPHome](https://esphome.io) device configurations.

I plan to write up more about it at some point. [Follow me on Twitter](https://twitter.com/soffes) if you want to follow along.

## About my setup

### Installation

I run Home Assistant in [Docker on my Synology NAS](https://www.home-assistant.io/docs/installation/docker/#synology-nas). It works really well!

This git repo is the `/config` directory that the container mounts. I use the `make` command in the Makefile to upload and validate the configuration when I make a change and then `make restart` to restart the container if everything is good.

### HomeKit

I really like Apple's Home app and the Siri integration that comes with it. My wife also likes using the home app over something like the Home Assistant app. 

My approach is to link everything directly to Home Assistant and then expose some devices to HomeKit from HomeAssistant. I do this with a whitelist so I can make sure everything in HomeKit is configured and will have a good experience in the Home app.

### Siri Shortcuts

I have a UniFi router and use it to configure a URL with Dynamic DNS for my house (and I’m not going to tell you what that is :P). I also exposed port forwarding for port `8123` to my Synology so I can reach Home Assistant externally.

Then you can follow this [simple guide](https://community.home-assistant.io/t/ios-shortcuts-with-ha-no-ssl-required/89529) to create a Siri Shortcut to do things. I made one that hits `/api/services/script/sonos_pause_all` so I can yell "Hey Siri, stop Sonos"! This is great for things you want to be able to control with Siri but don’t want to expose in the Home app.

## Questions?

Have questions about my setup? [Tweet me](https://twitter.com/soffes)!
