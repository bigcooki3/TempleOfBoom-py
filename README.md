# [TempleOfBoom-py](https://docs.google.com/spreadsheets/d/1uI3EbFX6dp08mc0wS7lJR-cYdJcEJLrdYgNfSphR3vE/edit#gid=1688117650)
A Python script that reads a Spotify playlist, ['Temple Of Boom'](https://open.spotify.com/user/1218301181/playlist/5FtOlVibocfmgupPnZGKDS), and dumps it to a Google sheet for archiving each week. Managed by a cron job on my personal Linux server to run every Thursday at 10:30 AM, EST.

# Dependencies
[Spotipy](https://github.com/plamere/spotipy)

[Google Spreadsheets Python API v4](https://github.com/nithinmurali/pygsheets)

You need to have a valid service-creds.json file from the Google Sheets API, and Spotify Developer Client Credentials to run.