"""
paseo_guns.py
-------------
Entry point for the Paseo Guns store management system.

Usage:
    python paseo_guns.py
"""

from gun_store.cli import GunStoreCLI


def main() -> None:
    cli = GunStoreCLI()
    cli.run()


if __name__ == "__main__":
    main()
