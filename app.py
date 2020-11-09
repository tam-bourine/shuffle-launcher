import os
from slack_bolt import App
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = App(
    token = os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/shuffle")
def open_modal(ack, say, command):
    ack()
    say('本来ならモーダルが開く')

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
