import os
from slack_bolt import App
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = App(
    token = os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
)
@app.command("/shuffle")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # say('本来ならモーダルが開く')
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receving it
        trigger_id = body["trigger_id"],
        # View payload
        view = {
            "title": {
                "type": "plain_text",
                "text": "shuffle-launcher",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": " *shuffle-launcher* はslackのメンバーをシャッフルしてグループ分けしてくれるアプリです"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "グループあたりの人数",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "checkboxes",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "前回のグループ分けを考慮しない（サンプル）",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "前々回のグループ分けを考慮しない（サンプル）",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "スプレッドシートを作成しない（サンプル）",
                                    "emoji": True
                                },
                                "value": "value-2"
                            }
                        ],
                        "action_id": "checkboxes-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "設定",
                        "emoji": True
                    }
                }
            ]
        }
    )

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
