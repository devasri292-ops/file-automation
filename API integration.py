import requests

print("=== Country Information Search ===")

while True:
    country_name = input("\nEnter country name (or 'exit' to quit): ").strip()

    if country_name.lower() == "exit":
        print("Goodbye!")
        break

    try:
        url = f"https://countriesnow.space/api/v0.1/countries/population/cities"

        response = requests.get(url)
        data = response.json()

        found = False

        for item in data["data"]:
            if country_name.lower() in item["country"].lower():
                print("\nCountry:", item["country"])
                print("City:", item["city"])
                print("Population:", item["populationCounts"][-1]["value"])
                print("-" * 40)
                found = True
                break

        if not found:
            print("Country not found.")

    except Exception as e:
        print("Error:", e)