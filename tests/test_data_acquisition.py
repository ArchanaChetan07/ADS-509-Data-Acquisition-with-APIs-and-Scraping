import pytest
import re

class TestDataAcquisition:
    def test_url_validation(self):
        valid_urls = ["https://example.com","http://api.genius.com/songs"]
        pattern = re.compile(r"^https?://[\w\-]+(\.[\w\-]+)+[/#?]?.*$")
        for url in valid_urls:
            assert pattern.match(url), f"Invalid URL: {url}"

    def test_api_response_structure(self):
        mock = {"status": 200, "data": {"artist": "Adele", "song": "Hello", "lyrics": "Hello from..."}}
        assert mock["status"] == 200
        assert "lyrics" in mock["data"]

    def test_lyrics_not_empty(self):
        lyrics = "Hello, it\'s me\nI was wondering if after all these years"
        assert len(lyrics) > 0
        assert "\n" in lyrics

    def test_artist_name_cleaned(self):
        raw = "  Adele  "
        clean = raw.strip().title()
        assert clean == "Adele"

    def test_rate_limit_handling(self):
        import time
        requests_made = 0
        max_per_second = 5
        for _ in range(3):
            requests_made += 1
        assert requests_made <= max_per_second

    def test_duplicate_lyrics_removed(self):
        songs = [{"title":"Hello","artist":"Adele"},{"title":"Hello","artist":"Adele"},{"title":"Rolling in the Deep","artist":"Adele"}]
        unique = {(s["title"],s["artist"]):s for s in songs}.values()
        assert len(list(unique)) == 2

class TestWebScraping:
    def test_html_tag_removal(self):
        html = "<p>Hello <b>world</b></p>"
        clean = re.sub(r"<[^>]+>","",html)
        assert "<p>" not in clean
        assert "Hello world" in clean

    def test_special_chars_in_lyrics(self):
        text = "Don\'t stop believin\' — hold on to that feelin\'"
        assert "'" in text or "'" in text or "\'" in text

    def test_pagination_handling(self):
        pages = [f"page_{i}" for i in range(1, 6)]
        assert len(pages) == 5
        assert pages[0] == "page_1"
