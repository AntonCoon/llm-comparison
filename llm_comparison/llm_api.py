from typing import Dict

import requests


def ask_model(prompt: str, model: str, BASE_URL: str, headers: Dict[str, str]):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000,
        "temperature": 0.1,
    }
    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Failed: {str(e)}"
