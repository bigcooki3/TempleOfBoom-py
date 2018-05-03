import datetime
import pygsheets as ps
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials


def print_tracks(sheet, tracks):
    # Appends playlist results to Google sheet
    sheet.insert_rows(3, 1, values=['Artist', 'Track', 'User'])
    for i, item in enumerate(tracks['items'][1:]):
        track = item['track']
        user = item['added_by']
        username = spot.user(user['id'])
        if username['display_name'] is not None:
            username = username['display_name']
        else:
            username = user['id']
        sheet.insert_rows(
            row=4 + i,
            number=1,
            values=[
                track['artists'][0]['name'],
                track['name'],
                username
            ]
        )
    sheet.insert_rows(i + 5, 1)
    sheet.cell('A4').set_text_format('bold', True)
    sheet.cell('B4').set_text_format('bold', True)
    sheet.cell('C4').set_text_format('bold', True)
    return i


def main():
    # Open spreadsheet and current worksheet
    doc = gs.open_by_key('1uI3EbFX6dp08mc0wS7lJR-cYdJcEJLrdYgNfSphR3vE')
    sheet = doc[0]

    # Select playlist ID and username
    uri = 'user/1218301181/playlist/5FtOlVibocfmgupPnZGKDS'
    masteruser = uri.split('/')[1]
    playlist_id = uri.split('/')[3]

    # Pull playlist results and make space for it
    results = spot.user_playlist(masteruser, playlist_id)
    tracks = results['tracks']

    # Print header with Monday's date
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    sheet.insert_rows(2, 1, values=[monday.strftime("Week of %B %d, %Y")])

    # Print tracks
    i = print_tracks(sheet, tracks)
    print("Completed successfully.")


# Open credentials for Spotify and Google Sheets API
gs = ps.authorize(service_file='service-creds.json')
spcredentials = SpotifyClientCredentials()
spot = sp.Spotify(client_credentials_manager=spcredentials)
spot.trace = True

if __name__ == "__main__":
    main()
