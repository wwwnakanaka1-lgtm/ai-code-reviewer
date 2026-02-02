"""テスト用のコード（意図的に問題を含む）"""

import os

def get_user_data(user_id):
    # SQLインジェクションの脆弱性
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def divide(a, b):
    # ゼロ除算のチェックなし
    return a / b

def process_items(items):
    result = []
    for i in range(len(items)):  # 非Pythonicなループ
        result.append(items[i] * 2)
    return result

password = "admin123"  # ハードコードされたパスワード
