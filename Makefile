# Synology host
SERVER=archive.local
SSH_PORT=49160

# Check the configuration
.PHONY: check
check:
	@ssh $(SERVER) -p $(SSH_PORT) "sudo /usr/local/bin/docker exec homeassistant python -m homeassistant --script check_config --config /config"

# Restart Home Assistant
.PHONY: restart
restart:
	@ssh $(SERVER) -p $(SSH_PORT) "sudo /usr/local/bin/docker restart homeassistant"

# Lint YAML
.PHONY: lint
lint:
	@yamllint --version >/dev/null 2>&1 || pip3 install yamllint
	@yamllint -c .yamllint.yaml .
