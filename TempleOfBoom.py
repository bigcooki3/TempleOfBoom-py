import datetime
import pygsheets as ps
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials


def print_tracks(sheet, tracks):
    # Appends playlist results to Google sheet
    sheet.insert_rows(3, 1, values=['Artist', 'Track'])
    for i, item in enumerate(tracks['items']):
        track = item['track']
        sheet.insert_rows(
            row=4 + i,
            number=1,
            values=[track['artists'][0]['name'], track['name']]
        )
    sheet.insert_rows(i + 5, 1)
    sheet.cell('A4').set_text_format('bold', True)
    sheet.cell('B4').set_text_format('bold', True)
    return i


def main():
    # Open credentials for Spotify and Google Sheets API
    gs = ps.authorize(service_file='service-creds.json')
    spcredentials = SpotifyClientCredentials()
    spot = sp.Spotify(client_credentials_manager=spcredentials)

    # Open spreadsheet and current worksheet
    doc = gs.open_by_key('1uI3EbFX6dp08mc0wS7lJR-cYdJcEJLrdYgNfSphR3vE')
    sheet = doc[0]

    # Select playlist ID and username
    uri = 'user/1218301181/playlist/5FtOlVibocfmgupPnZGKDS'
    username = uri.split('/')[1]
    playlist_id = uri.split('/')[3]

    # Pull playlist results and make space for it
    results = spot.user_playlist(username, playlist_id)
    tracks = results['tracks']

    # Print header with Monday's date
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    sheet.insert_rows(2, 1, values=[monday.strftime("Week of %B %d, %Y")])

    # Print tracks
    i = print_tracks(sheet, tracks)
    print("Completed successfully.")


if __name__ == "__main__":
    main()
