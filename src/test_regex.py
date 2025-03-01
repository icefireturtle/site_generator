import unittest
from regex import extract_markdown_images, extract_markdown_links

class TestRegEx(unittest.TestCase):

    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This a sentence with an image ![image](https://imgur.com/madesomeupZzXqc.png)"
        )
        self.assertListEqual([("image", "https://imgur.com/madesomeupZzXqc.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This a sentence with a [link](https://imgur.com/ZzXqDmadesomemoreup.png)"
        )
        self.assertListEqual([("link", "https://imgur.com/ZzXqDmadesomemoreup.png")], matches)

if __name__ == "__main__":
    unittest.main()