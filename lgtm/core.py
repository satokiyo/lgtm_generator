# coding:utf_8

import click


@click.command()
@click.option(
    "--message", "-m", default="LGTM", show_default=True, help="画像にオーバーレイする文字列"
)
@click.argument("keyword")
def cli(keyword, message):
    """LGTM画像作成ツール"""
    lgtm(keyword, message)

    click.echo("lgtm")  # 動作確認用


def lgtm():

    #  ここにロジックを追加していく
    pass
