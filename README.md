# Steam AppID Changer

Steam AppID Changer is a simple utility script that allows you to change the AppID of a Steam game and launch it with a modified AppID. The script is designed to be run as a standalone executable (.exe) on Windows.

Puedes leer esto también en [Español](https://github.com/Kioraga/steam-appid-changer/blob/main/README.es.md).

## Getting Started

To use the Steam AppID Changer, follow these steps:

1.  Download the latest release of the script as a standalone executable from the [Releases](https://github.com/Kioraga/steam-appid-changer/releases) section of this repository.

2.  Before running the script, make sure you have a `config.ini` file in the same directory as the executable. The configuration file should specify the necessary details such as the game's installation path, name, process name, and the desired AppID to patch.

3.  Double-click the executable to run the Steam AppID Changer.

If you want to see terminal output during execution, you can run the executable with the `--show-output` flag. Otherwise, the script's GUI will be hidden.

## Configuration

The `config.ini` file contains the following sections and options:

```ini
[Game Target]
path = Path to the game's installation directory
name = Game name
process = Name of the game's executable process
appid = Original Steam AppID for the game

[Patch]
patch_appid = New Steam AppID to use temporarily
```

Ensure that you have correctly set up the `config.ini` file with the appropriate values before running the script.

## Dependencies

The Steam AppID Changer executable does not require any external dependencies to run. It is a self-contained script that interacts with the Steam appid file and the game executable.

## License

This project is licensed under the [MIT License](https://github.com/Kioraga/steam-appid-changer/blob/main/LICENSE).

## Disclaimer

This script modifies game files and is intended for educational and testing purposes only. Use it responsibly and at your own risk. The author and contributors are not responsible for any damage caused by the usage of this script.
