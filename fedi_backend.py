import os.path
import sys
from mastodon import Mastodon

### GLOBAL VARIABLES
APP_FILE_EXT = ".secret"

class FediPoster:
	"""
	Logs in and holds onto Fedi account credentials
	allowing posting to a Fedi account
	TODO: don't always hold onto keys and secrets
	"""

	def __init__(self, instance_url = "", username = "", client_key = "", client_secret = "", client_token = ""):
		self._url = self._format_url(instance_url)
		self._username = username
		self._client_key = client_key
		self._client_secret = client_secret
		self._client_token = client_token
		self._api = None
		self._login()

	def _format_url(self, url = ""):
		"""
		Format the provided url to ensure compatiblity
		"""
		return url

	def _login(self):
		"""
		Attempt to login to the provided instance!
		"""
		if not os.path.isfile(APP_FILE):
			self._create_app()

		login_count = 0
		while (not self._api and login_count < 3):
			try:
				self._api = Mastodon(client_id = self._url + APP_FILE_EXT, api_base_url = "https://" + self._url)
				self._api.log_in(token = ?, to_file = self._username + APP_FILE_EXT)
			except:
				print("!!! - Login %i failed" % (login_count))
				self._api = None
				login_count += 1

		if not self._api:
			print("!!! - Login failed. Exiting")
			sys.exit(1)

	def _create_app(self):
		"""
		If instance has never been logged into before,
		create application and store as file for future use
		"""
		result = Mastodon.create_app("toot_bot", api_base_url = "https://" + self._url, to_file = self._url + APP_FILE_EXT)
		if result:
			print("toot_bot app created on instance: " + self._url)
		else:
			print("!!! - Failed to create app on instance: " + self._url)
			sys.exit(1)

	def post(self, post_text = "", sensitive = False, visibility = "", spoiler_text):
		"""
		Post a status!
		TODO: add support for toot media and replies
		"""
		self._api.status_post(in_reply_to_id = None, sensitive = False, visibility = visibility, spoiler_text = spoiler_text)