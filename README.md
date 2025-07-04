Automated end-to-end test for verifying cookie consent (e.g., accepting analytics cookies) and checking that the correct cookies are stored in the browser. The test can be run in multiple browsers simultaneously (Chromium, Firefox, WebKit).

1. Features

- Visits a specified website.
- Accepts selected (e.g., analytics) cookies via the cookie banner.
- Verifies that the relevant cookies are set in the browser storage.
- Supports running in Chromium, Firefox, and WebKit.
- Easy to configure and extend.

2. Requirements

- Python 3.8 or newer
- pip

3. Installation

- Clone the repository:
  git clone https://github.com/Sajmox/cookie-consent-playwright.git
  cd cookie-consent-playwright

- Install dependencies:
  pip install -r requirements.txt
  python -m playwright install

- Running the Test in a single browser:
  (You can replace chromium by webkit or firefox)
  task test-chromium

- Run in multiple browsers:
  task test-all
