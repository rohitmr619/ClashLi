import requests
import argparse
import time
from tabulate import tabulate

def print_ascii_art():
    print(r"""
      _____ _           _     _      
     / ____| |         | |   (_)   
    | |    | | __ _ ___| |    _  
    | |    | |/ _` / __| |   | |
    | |____| | (_| \__ \ |___| |_
     \_____|_|\__,_|___/\_____/_/

            TOOL BY ROHIT M R
              
    """)

def get_player_stats(player_id):
    api_token = "TOKEN"  # Replace this with your actual API token
    url = f"https://api.clashroyale.com/v1/players/%23{player_id}"  # '#' is URL-encoded as '%23'
    headers = {"Authorization": f"Bearer {api_token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def display_menu():
    print("\n=== Clash Royale Stats Menu ===")
    print("1. View Player Stats")
    print("2. View Player Cards")
    print("3. Exit")

def display_player_cards(cards):
    if not cards:
        print("No cards available.")
        return
    
    print("\n=== Player Cards ===")
    
    rarity_dict = {}
    for card in cards:
        rarity = card.get("rarity", "Unknown")
        if rarity not in rarity_dict:
            rarity_dict[rarity] = []
        rarity_dict[rarity].append([card.get("name", "Unknown"), card.get("level", "N/A")])
    
    for rarity, card_list in rarity_dict.items():
        print(f"\n--- {rarity.upper()} CARDS ---")
        table_data = []
        for i in range(0, len(card_list), 5):
            row = [f"{card_list[j][0]} (Lvl {card_list[j][1]})" if j < len(card_list) else "" for j in range(i, i+5)]
            table_data.append(row)
        print(tabulate(table_data, tablefmt="grid"))

def main():
    print_ascii_art()
    player_id = input("Enter your Clash Royale Player ID (without the #): ")
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            stats = get_player_stats(player_id)
            if stats:
                print("\n=== Player Stats ===")
                print("Player Name:", stats.get("name", "N/A"))
                print("Tag:", stats.get("tag", "N/A"))
                print("Trophies:", stats.get("trophies", "N/A"))
                print("Best Trophies:", stats.get("bestTrophies", "N/A"))
                print("Level:", stats.get("expLevel", "N/A"))
                print("Wins:", stats.get("wins", "N/A"))
                print("Losses:", stats.get("losses", "N/A"))
                print("Clan Name:", stats.get("clan", {}).get("name", "No Clan"))
            time.sleep(2)
        elif choice == "2":
            stats = get_player_stats(player_id)
            if stats:
                display_player_cards(stats.get("cards", []))
            time.sleep(2)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()