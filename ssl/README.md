To renew certs, start certbot:

```sh
$ sudo certbot certonly --manual
```

Once you get the challenge, update `app.rb` and then run:

```sh
$ bundle exec shotgun -o 0.0.0.0
```

Then enable port forwarding to local IP for the port shotgun is running and continue in certbot. Disable port forwarding after.
