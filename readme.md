# Hurricane Electric DNS authenticator plugin for certbot

This plugin for certbot allows using the dns-01 challenge with Hurricane Electric's DDNS interface for setting TXT records.

## setup

In order to use this plugin you first need to have created the _acme-challenge TXT record for your domain.

1. Login to [Hurricane Electric DNS](https://dns.he.net).
2. Create a new TXT record for your domain
    * Make sure to check "Enable entry for dynamic dns"
3. Generate a new DDNS secret by clicking on the "Generate a DDNS key" icon


## credentials

The plugin stores your DDNS secret in credentials INI file which gets passed to certbot.

```ini
dns_he_secret=<dns_secret>
```

where `<dns_secret>` is the previously generated DDNS key from before.
Make sure to set the permissions of this file to 0700 using `chmod 0700 <filename>`

## usage

Once you have the _acme-challenge record created and the credentials file written you can generate a cert for your domain using the following command:
```bash
certbot certonly \
--authenticator dns-he \
--dns-he-credentials <credential file> \
-d <domain>
```
