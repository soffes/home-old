To renew certs, start certbot:

```sh
$ sudo certbot certonly --manual
```

Once you get the challenge run:

```sh
$ bundle exec rake "server[challenge.asdf...]"
```

Then enable port forwarding to local IP for the port shotgun is running and continue in certbot. Disable port forwarding after.

After completing the the flow, the certificates will be in `/etc/letsencrypt/live/domain_name_here/`. Copy `fullchain.pem` and `privkey.pem` to the `ssl` directory (this directory) where Home Assistant is running and restart.
