import json
from fuzzywuzzy import fuzz, process
from tabulate import tabulate

# Load election results data from the local resultat.json file
def load_election_data(filename='resultat.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: The resultat.json file was not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: There was an issue decoding the JSON file.")
        exit(1)

# Fuzzy search for a city or municipality
def find_city(data, city_name):
    city_names = list(data.keys())
    matches = process.extract(city_name, city_names, limit=5, scorer=fuzz.partial_ratio)
    
    # If no matches with a high score, return None
    if matches and matches[0][1] > 80:  # Threshold for fuzzy match
        return matches[0][0]
    return None

# Get and display election results for the city
def display_election_results(data, city_name):
    # Find the closest match to the input city name
    city = find_city(data, city_name)
    if not city:
        print(f"Error: No matching city found for '{city_name}'.")
        return
    
    # Retrieve the election results for the found city
    results = data.get(city, {}).get('2024', None)
    if not results:
        print(f"Error: No election results found for {city}.")
        return
    
    # Prepare results for display
    print(f"\nElection Results for {city} (2024):\n")
    print("Party | Votes | Percentage")
    print("-" * 40)
    
    # Sort by votes in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    # Format the results into a clean table
    table_data = [(party, votes, f"{(votes / sum(results.values())) * 100:.2f}%") for party, votes in sorted_results]
    
    # Output using the tabulate module for nice formatting
    print(tabulate(table_data, headers=["Party", "Votes", "Percentage"], tablefmt="pretty"))
    
    # Check if city is part of a larger municipality or region
    region_info = data.get(city, {}).get('Region', 'N/A')
    if region_info != 'N/A':
        print(f"\nNote: This city is part of the larger municipality or region: {region_info}")

# Main function to run the program
def main():
    # Load election data
    data = load_election_data()
    
    # User input for city/municipality name
    city_name = input("Enter the name of a Swedish city or municipality: ").strip()
    
    # Display election results for the given city
    display_election_results(data, city_name)

if __name__ == "__main__":
    main()
