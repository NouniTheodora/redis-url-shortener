from insertion import insert_url
from query import query_short_url
from statistics import get_user_stats, get_average_views

def main():
    print("Welcome to Redis URL Shortener")
    username = input("Please enter your username or email: ").strip()

    while True:
        print("\n--- Menu ---")
        print("1. Insert new URL")
        print("2. Query short URL")
        print("3. Show statistics")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            long_url = input("Enter long URL: ")
            print(insert_url(long_url, username))
        elif choice == "2":
            short_code = input("Enter short code: ")
            print(query_short_url(short_code))
        elif choice == "3":
            print(get_user_stats(username))
            print(get_average_views())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()