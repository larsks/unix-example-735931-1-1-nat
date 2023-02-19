#!/usr/bin/env python3

import click
import subprocess
import time
import yaml


@click.command
@click.option("-t", "--target", default="")
@click.option("-k", "--key-interval", type=float, default=0.2)
@click.option("-l", "--line-interval", type=float, default=1)
@click.option("-s", "--after-interval", type=float, default=2)
@click.argument("scriptname")
def main(target, line_interval, key_interval, after_interval, scriptname):
    with open(scriptname) as fd:
        script = yaml.safe_load(fd)

    for action in script:
        for pane in action["panes"]:
            pane = f"{target}.{pane}"
            for line in action.get("lines", []):
                subprocess.check_call(
                    ["tmux", "send-keys", "-t", pane, line, "Enter"],
                )
                time.sleep(action.get("line_interval", line_interval))
            for keys in action.get("keys", []):
                subprocess.check_call(
                    ["tmux", "send-keys", "-t", pane] + keys.split(),
                )
                time.sleep(action.get("key_interval", key_interval))

        time.sleep(action.get("after_interval", after_interval))


if __name__ == "__main__":
    main()
