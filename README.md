
# About OpenGUIlion

OpenGUIlion is a very basic application written in Python that only does one thing: it shows non-interactive, animated GUIs from the "Evangelion" franchise.

## Features

- Recreated interfaces from the computers and screens seen in "Evangelion", stretched to 2:1.
- Runs in Python 3.

## Requirements

To run OpenGUIlion you need Python 3 with PyGame and PIL available. Some distros already include them, but in case yours doesn't you can easily install them through `pip`.

You also need some extra fonts that must be placed under the `/openguilion/fonts/` folder and cannot be included in the repo for copyright reasons, whereas others can. How to get the copyrighted fonts is up to you and I will not provide further instructions nor direct downloads.

- Obtain "Helvetica Narrow Bold Regular" and name it `helvet.ttf`.
- Obtain "Helvetica Bold" and name it `helvetb.ttf`.
- Obtain "EVA-Matisse_Classic EB" and name it `matisse.ttf`. Since it has been published in the Internet Archive I do not consider illegal to link it. [Get it here.](https://archive.org/details/qjwi3h)

You could try to use Arial Narrow and Arial Bold as replacements for Helvetica, but I have not tested these cases.

## How to run

You can directly run `openguilion.py` from the command line. The program does not accept any arguments as of now. It has been tested under Python 3.9.

## Future developments

- Additional scenes.
- Adapt the code so the app can be properly displayed in Waveshare's 6in flexible AMOLED screen.

## About the author

This software has been made by [stage7](https://www.github.com/stage7). You can also [ping me on Twitter](https://twitter.com/s7age) if you need help or just say "hello".

The project's official Twitter account is [@OpenGUIlion](https://twitter.com/openguilion).

## License

This software is distributed under a [GPL 3.0 license](https://opensource.org/licenses/GPL-3.0).

## Disclaimer

All names are trademarks of their respective owners and are used here under fair use.

- "Evangelion" is a trademark of Gainax Corporation and Khara Inc.
- "Helvetica" is a trademark of Monotype Imaging Inc.
- "ITC Matisse®" is a trademark of Monotype ITC Inc.

Sinkin Sans is used under an [Apache License](https://www.fontsquirrel.com/license/sinkin-sans).
