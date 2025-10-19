# Cloud Coding Agentの環境構築例

以下のサービスではDevContainerは利用できない。
それぞれの方法で環境構築が必要になる。

## GitHub Copilot Coding Agents

GitHub Actionsを利用して構築する

https://docs.github.com/ja/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

[.github/workflows/copilot-setup-steps.yml](.github/workflows/copilot-setup-steps.yml) に記述する。

以下のプロンプトを実行すると、uvを使ってテストが実行できていることを確認できた。

```
タスクの削除API `DELETE /api/tasks/<int:task_id>` を実装して。
実装後に、他に影響がないか、全体でテストを実行して。
```

## Codex

以下のイメージのコンテナが使われる。
現在はコンテナイメージの変更は不可能。

> https://github.com/openai/codex-universal

環境設定の画面で、セットアップスクリプトを指定できる。
セットアップスクリプトはリポジトリチェックアウト後に呼ばれるため、リポジトリ内にスクリプトを置き、そのパスを指定しておくこともできる。

セットアップスクリプトに、以下を指定した。

```
./setup_script_for_codex.sh
```

以下のプロンプトを実行すると、uvを使ってテストが実行できていることを確認できた。

```
タスクの削除API `DELETE /api/tasks/<int:task_id>` を実装して。
実装後に、他に影響がないか、全体でテストを実行して。
```

## Jules

非公開のVMイメージが使われる。現在はVMイメージの変更は不可能。

環境設定の画面で、セットアップスクリプトを指定できる。
セットアップスクリプトはリポジトリチェックアウト後に呼ばれるため、リポジトリ内にスクリプトを置き、そのパスを指定しておくこともできる。

セットアップスクリプトに、以下を指定した。

```
./setup_script_for_jules.sh
```

以下のプロンプトを実行すると、uvを使ってテストが実行できていることを確認できた。

```
タスクの削除API `DELETE /api/tasks/<int:task_id>` を実装して。
実装後に、他に影響がないか、全体でテストを実行して。
```