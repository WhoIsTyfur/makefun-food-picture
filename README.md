# Food picture entry for make.fun `food-picture-01`

An entry for the make.fun bounty [Make the best-looking food picture](https://make.fun/bounty/food-picture-01).

## What it does

`main.py` (Python 3.13, standard library only) copies `food.jpg`, a 1024x1024 photoreal food image, byte for
byte to `/output/entry.png`. The file is a JPEG; the contest tells PNG and JPEG apart by their first bytes, so
the name stays `entry.png`. The image was made with an image model, then downscaled to 1024x1024 and re-encoded
as a baseline JPEG (quality 95, no chroma subsampling, no metadata) to fit the gate: at most 1 MiB and at most
1024 by 1024 pixels.

## How it is scored

A sealed gate checks the file is a whole PNG or JPEG within those limits. Valid entries then go before an AI
judge that compares pictures two at a time, weighing in order: does it make you hungry; does the food look
fresh, real and well made (steam, gloss, crunch, melt); styling and light; clean craft with no artefacts; and
whether it still reads at about 300 pixels across. Entries rank by Bradley-Terry win rate over a Swiss heat and
a playoff.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`out/entry.png` is then the exact file the judge sees. Running it twice gives the same bytes.
