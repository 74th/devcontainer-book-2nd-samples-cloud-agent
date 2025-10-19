## API

- `GET /api/tasks` : タスク一覧の取得
- `POST /api/tasks` : タスクの追加
- `PATCH /api/tasks/<int:task_id>/done` : タスクの完了

## 開発時に利用するコマンド

- テスト実行 `uv run python -m unittest discover -s todo_api -t . -p "*_test.py" -v`
- APIの起動 `uv run python -m todo_api.server.api`