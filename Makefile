# Synology host
SERVER=archive.local

# Path to the configuration on Synology
REMOTE_CONFIG=/volume1/docker/hass/homeassistant

# Copy the config to the server
.PHONY: install
install:
	@rsync -hrPt -e ssh --rsync-path=/bin/rsync --exclude .git --exclude .storage . $(SERVER):$(REMOTE_CONFIG)
	@$(MAKE) check

.PHONY: default
default: install ;

# Check the configuration
.PHONY: check
check:
	@ssh $(SERVER) "sudo /usr/local/bin/docker exec homeassistant python -m homeassistant --script check_config --config /config"

# Restart Home Assistant
.PHONY: restart
restart:
	@ssh $(SERVER) "sudo /usr/local/bin/docker restart homeassistant"

# ESPHome dashboard
.PHONY: esphome
esphome:
	@esphome esphome dashboard

# Lint YAML
.PHONY: lint
lint:
	@yamllint --version >/dev/null 2>&1 || pip3 install yamllint
	@yamllint -c .yamllint.yaml .
