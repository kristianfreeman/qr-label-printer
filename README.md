# QR Label Printer

This Python project allows you to generate layouts of QR codes into a PDF file. That file is printed onto label paper.

Currently, I use this to generate a 4x5 layout of QR codes to label boxes in storage. The write up for that will come soon!

This project doesn't handle multiple layouts/page types. You could probably implement that yourself without too much trouble.

Also, this project was written with ChatGPT. Complain to OpenAI if the code is bad. :)

## Usage

```sh
$ git clone https://github.com/kristianfreeman/qr-label-printer
$ cd qr-label-printer
$ cp config.json.example config.json
$ vim config.json # Update config to your desired layout
$ python main.py
$ open out/stickers.pdf
```
