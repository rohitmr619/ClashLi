# CLASHLi - Clash Royale CLI Stats Tool

CLASHLi is a command-line interface (CLI) tool that fetches and displays Clash Royale player statistics, including player info and card collection details.

## Features
- View player stats: trophies, level, wins/losses, clan info, etc.
- Display owned cards.


### Install Required Libraries
Run the following command to install necessary dependencies:
```sh
pip install requests tabulate
```

## Setup API Token
This tool requires a Clash Royale API token for authentication. Follow these steps to obtain and set it up:

1. Visit [Clash Royale API](https://developer.clashroyale.com/) and sign in.
2. Create an API key from the "My Keys" section.
3. Copy the API token.
4. Replace `YOUR_API_TOKEN` in the script with your actual API token:
   ```python
   api_token = "YOUR_API_TOKEN"
   ```

## Usage
Run the script using:
```sh
python clashli.py
```
Follow the prompts to enter your player ID (without the `#`) and navigate through the menu.

## Example Output
```
      _____ _           _     _      
     / ____| |         | |   (_)   
    | |    | | __ _ ___| |    _  
    | |    | |/ _` / __| |   | |
    | |____| | (_| \__ \ |___| |_
     \_____|_|\__,_|___/\_____/_/

            TOOL BY ROHIT M R

Enter your Clash Royale Player ID (without the #):

=== Clash Royale Stats Menu ===
1. View Player Stats
2. View Player Cards
3. Exit
```

## License
This project is open-source. Feel free to modify and contribute.

## Author
Developed by **Rohit M R**.

