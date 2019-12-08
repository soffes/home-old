SERVER=archive.local
REMOTE_CONFIG=/volume1/docker/homeassistant-config

# Copy the config to the server
.PHONY: install
install:
	@rsync -azh -e ssh --rsync-path=/bin/rsync --exclude .git --exclude-from="$(git -C . ls-files --exclude-standard -oi --directory >.git/ignores.tmp && echo .git/ignores.tmp)" . $(SERVER):$(REMOTE_CONFIG)
	@$(MAKE) check

.PHONY: default
default: install ;

# Check the configuration
.PHONY: check
check:
	@ssh $(SERVER) "sudo /usr/local/bin/docker exec homeassistant python -m homeassistant --script check_config --config /config"

# Restart Home Assistant
restart:
	@ssh $(SERVER) "sudo /usr/local/bin/docker restart homeassistant"
