"""DNS Authenticator using Hurricane Electric's DDNS interface."""
import logging
import requests

from certbot import errors
from certbot.plugins.dns_common import DNSAuthenticator

logger = logging.getLogger(__name__)

class Authenticator(DNSAuthenticator):
    """DNS Authenticator for Hurricane Electric

    This Authenticator uses Hurricane Electric's DDNS interface for the dns-01 challenge.
    """
    description = ('Obtain certificates using a DNS TXT record (if you are using Hurricane Electric for DNS).')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):
        super().add_parser_arguments(add, default_propagation_seconds=30)
        add('credentials', help='Hurrican Electric ddns credential file')

    def more_info(self):
        return (
            'This plugin can be used to authenticate a domain using Hurrican eletric DDNS updates.'
        )

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'Hurricane Electric credentials INI file',
            {
                'secret': 'Hurricane Electric ddns secret'
            }
        )

    def _get_client(self, secret):
        return DDNS("https://dyn.dns.he.net/nic/update", secret)

    def _perform(self, domain, validation_name, validation):
        client = self._get_client(self.credentials.conf("secret"))
        client.set_txt_record(validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        client = self._get_client(self.credentials.conf("secret"))
        client.reset_txt_record(validation_name)


class DDNS(object):
    """
    DDNS Client
    """
    def __init__(self, url, secret):
        self.url = url
        self.secret = secret

    def set_txt_record(self, validation_name, validation):
        self._post_request(validation_name, validation)

    def reset_txt_record(self, validation_name):
        self._post_request(validation_name, "None")

    def _post_request(self, validation_name, validation):
        data = {
            "hostname": validation_name,
            "txt": validation,
            "password": self.secret
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Certbot-DDNS',
        }
        requests.post(url=self.url, headers=headers, data=data).raise_for_status()

