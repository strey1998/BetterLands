# BetterLands.py

Python script which takes in an XMage deck and spits out an XMage deck with your preferred printings of cards. Contrary to the title, it works with all cards, not just lands.

### Usage

Run ```python3 BetterLands.py -i <input deck> -o <output deck>```. If ```<output deck>``` is unspecified, it defaults to the same filename with a "-BL" tagged at the end. If you specify the same filename, it WILL overwrite the original deck. Be careful.

### Configuration

Run ```python3 BetterLands.py --resetconfig``` to (re)generate the default config. This WILL overwrite any custom settings. Be careful.

If you run ```python3 BetterLands.py -a <input deck>```, it will not do anything to the deck, but it will take all of the cards in it and add (or overwrite) those preferences.

You can also manually add entries to the config file. The formatting is quite straightforward. Card names are not case sensitive.
