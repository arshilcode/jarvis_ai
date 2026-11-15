# import re
# import urllib.parse
# import urllib.request
# import webbrowser

# # Yahan apni pasand ke gaanon ki list add karte jao (naam hamesha small letters mein likhna)
# MUSIC_LIBRARY = {
#     "kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs",
#     "apna bana le": "https://www.youtube.com/watch?v=ElZfdU54Cp8",
#     "chaleya": "https://www.youtube.com/watch?v=VAdGW7QDJiU",
#     "tum hi ho": "https://www.youtube.com/watch?v=Umqb9KENgmk",
#     "pasoori": "https://www.youtube.com/watch?v=5Eqb_-j3FDA",
# }

# def play_song(query: str) -> str:
#     """Library se ya directly YouTube se gaana play karega"""
#     song_name = query.lower().strip()

#     # 1. Pehle tumhari personal library mein check karega
#     for title, url in MUSIC_LIBRARY.items():
#         if title in song_name or song_name in title:
#             webbrowser.open(url)
#             return f"Tumhari library se {title} play kar raha hoon."

#     # 2. Library mein nahi mila toh YouTube par top video dhundh kar chalayega
#     try:
#         encoded = urllib.parse.quote(song_name + " song")
#         search_url = f"https://www.youtube.com/results?search_query={encoded}"
#         req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
#         html = urllib.request.urlopen(req, timeout=5).read().decode("utf-8")
#         video_ids = re.findall(r"watch\?v=(\S{11})", html)

#         if video_ids:
#             webbrowser.open(f"https://www.youtube.com/watch?v={video_ids[0]}")
#             return f"YouTube par {song_name} chala raha hoon."
#     except Exception:
#         pass

#     # Fallback agar direct video ID na mile
#     webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(song_name)}")
#     return f"YouTube par {song_name} search kar raha hoon."





import re
import urllib.parse
import urllib.request
import webbrowser

SONGS = {
    "kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs",
    "apna bana le": "https://www.youtube.com/watch?v=ElZfdU54Cp8",
    "chaleya": "https://www.youtube.com/watch?v=VAdGW7QDJiU",
    "tum hi ho": "https://www.youtube.com/watch?v=Umqb9KENgmk",
    "pasoori": "https://www.youtube.com/watch?v=5Eqb_-j3FDA",
}


def play_song(query):
    name = query.lower().strip()

    for title, link in SONGS.items():
        if title in name or name in title:
            webbrowser.open(link)
            return f"Tumhari library se {title} play kar raha hoon."

    # Fallback to top YouTube search result
    try:
        q = urllib.parse.quote(f"{name} song")
        url = f"https://www.youtube.com/results?search_query={q}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=5).read().decode("utf-8")
        ids = re.findall(r"watch\?v=(\S{11})", html)

        if ids:
            webbrowser.open(f"https://www.youtube.com/watch?v={ids[0]}")
            return f"YouTube par {name} chala raha hoon."
    except Exception:
        pass

    webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(name)}")
    return f"YouTube par {name} search kar raha hoon."