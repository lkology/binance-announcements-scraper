import requests


def telegram_send_message(bot_token, user_id, html):    
    url = f"https://api.telegram.org/{bot_token}/sendMessage"

    payload={'chat_id': user_id, 'text': html, 'parse_mode': 'HTML', 'disable_web_page_preview': True}

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise RuntimeError(f"Failed to send Telegram alert, got status code: '{response.status_code}' and message: '{response.text}'")