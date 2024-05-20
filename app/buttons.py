from aiogram import types

from service import fetch_repositories

PROJECTS = [types.InlineKeyboardButton(text="🗂️ Projects", callback_data="projects")]

HELLO = [
    [
        types.InlineKeyboardButton(text="🔍 About me", callback_data="about"),
        types.InlineKeyboardButton(text="🛠️ Skills", callback_data="skills")
    ],
    [
        types.InlineKeyboardButton(text="📋 Resume", callback_data="resume"),
        types.InlineKeyboardButton(text="🗂️ Projects", callback_data="projects")
    ]
]
BACK = [types.InlineKeyboardButton(text="⬅️ Menu", callback_data="start")]
CV = [
    types.InlineKeyboardButton(text="📎 PDF", callback_data="resume_pdf"),
    # types.InlineKeyboardButton(text="🔗 Link", callback_data="link")
]


def button_from_repo(repo):
    return types.InlineKeyboardButton(text=repo.name, callback_data=f"repo_{repo.name}")


def sort_repositories_and_create_buttons():
    repos = fetch_repositories()
    kb_len = 2
    result = []
    for i in range(0, len(repos), kb_len):
        chunk = repos[i:i + kb_len]
        chunk = [button_from_repo(repo) for repo in chunk]
        result.append(chunk)
    return result


REPOSITORIES = sort_repositories_and_create_buttons() + [BACK]
