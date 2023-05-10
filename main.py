from codeoffer import oauth
from codeoffer import app

session = oauth.Session("10aa641e562bdd82d2f8449d")
token = session.create_session_token()
token.wait_for_confirmation()
app = app.App.by_session_token(token)
assets = app.get_asset_directory()
for asset in assets:
    print(f"{asset.name}: {asset.access}")
