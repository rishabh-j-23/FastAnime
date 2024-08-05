import click

from fastanime.cli.config import Config
from fastanime.cli.interfaces import anilist_interfaces
from fastanime.cli.utils.tools import QueryDict, exit_app

from ....anilist import AniList


@click.command(help="View anime you are watching")
@click.pass_obj
def watching(config: Config):
    if not config.user:
        print("Not authenticated")
        print("Please run: fastanime anilist loggin")
        exit_app()
    anime_list = AniList.get_anime_list("CURRENT")
    if not anime_list:
        return
    if not anime_list[0]:
        return
    media = [
        mediaListItem["media"]
        for mediaListItem in anime_list[1]["data"]["Page"]["mediaList"]
    ]  # pyright:ignore
    anime_list[1]["data"]["Page"]["media"] = media  # pyright:ignore
    anilist_config = QueryDict()
    anilist_config.data = anime_list[1]
    anilist_interfaces.select_anime(config, anilist_config)