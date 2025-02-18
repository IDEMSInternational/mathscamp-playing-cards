# Virtual Maths Camp Content Toolchain

This is a tool chain for converting content (puzzles, fun facts, games) from
Google Docs into various serving formats. It consists of a Google Apps script
and various python3 scripts.

## Setup

1. Ensure you have python >= 3.6 installed.

2. Install markdown for python: See https://python-markdown.github.io/install/
or https://pypi.org/project/Markdown/ 

3. Open the Google Docs "Content/Export test" in the Virtual maths camp Google
Drive folder. In the menu, select Tools -> Script Editor. The code editor
should already contain the content of `gdocs2md.gs` from this repository.
If it doesn't, paste it into the code editor and save it (File -> Save).
Then follow the installation instructions from the **Note** in
https://github.com/lmmx/gdocs2md-html

## Running the pipeline

The pipeline consists of various stages. 

### Google Docs to Markdown

Note: Deprecated. We will edit the Markdown files directly rather than
Google Docs, which is cumbersome and its conversion has issues.

---

Open the Google Docs "Content/Export test" in the Virtual maths camp Google
Drive folder. In the menu, select Tools -> Script Editor. 
Select `onInstall` from the functions dropdown menu and run it.
In the main document's menu, a *Markdown* should have appeared.
(Also see https://github.com/lmmx/gdocs2md-html for more details.)
Select Markdown -> Export to Markdown -> Export entire folder to local file.

This will create a Markdown subfolder within the Content folder, and
populate it with the content converted to Markdown format.

Note: If the script runs for longer than 6 minutes, you will get an error
saying that the script has timed out. You can simply rerun the script
multiple times until it has processed all content (indicated by a lack
of such error). This works as the script does not process already processed
content unless the corresponding GDoc file has been modified in the meantime.

### Markdown to json

Download the Markdown folder produced by the previous step, and place it in
your local copy of this repository. Run `md_to_json.py`.
This will create a `json/` folder containing each piece of content from
the Markdown folder converted to JSON, with extracted images.

### Various output formats.

If the version on this repo isn't up to date,
fill in `cards.csv` with the up-to-date mapping of cards to content.
(This is in the spreadsheet "Content/Content Tracker" on Google Drive.)

`make_flows.py` creates `generated_flows.json` with RapidPro flows
for the chatbot. Still needs testing. It also prints out which content
is still missing sections.

`make_booklet.py` creates a `booklet` folder containing `booklet.html` with the
content in a format suitable for the booklet accompanying the card deck.

`make_cards.py` creates a `cards` folder with all content relevant for designing
the cards.

`rescale.sh` takes the images in `json/images`, makes a copy of these
and rescales them (manually specified) and optimizes their file size.
Needs `convert` (https://legacy.imagemagick.org/) and `optipng`
(http://optipng.sourceforge.net/).

## Translation

Within this repo, get a copy of the translation files. In order to do this, run

```
git clone git@github.com:IDEMSInternational/vmc-translation-pipeline.git
```

In `make_booklet.py` and `make_cards.py`, change the `LANG` variable at the top
to the language of your choice. 

*Remark:* The source strings that are on Crowdin not in sync with the markdown files
in this branch and reflect the state as of commit `c8d0d09d99`.
To produce translated content, use the branch `crowdin-synched-fr` which reverts
these changes.