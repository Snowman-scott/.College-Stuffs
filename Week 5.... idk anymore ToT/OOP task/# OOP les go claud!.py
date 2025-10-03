# OOP les go claud!

class Person:
    def __init__(self, name):
        self.name = name
        self.sleep_data = []  # Store multiple nights of sleep
        self.calorie_data = []  # Store multiple days of calories
    
    def add_sleep(self, hours):
        self.sleep_data.append(hours)
    
    def add_calories(self, calories):
        self.calorie_data.append(calories)
    
    def average_sleep(self):
        if len(self.sleep_data) == 0:
            return 0
        return sum(self.sleep_data) / len(self.sleep_data)
    
    def average_calories(self):
        if len(self.calorie_data) == 0:
            return 0
        return sum(self.calorie_data) / len(self.calorie_data)
    
    def give_health_advice(self):
        avg_sleep = self.average_sleep()
        avg_calories = self.average_calories()
        
        print(f"\n--- Health Report for {self.name} ---")
        print(f"Average Sleep: {avg_sleep:.1f} hours per night")
        print(f"Average Calories: {avg_calories:.0f} per day")
        print("\nAdvice:")
        
        # Sleep advice
        if avg_sleep < 7:
            print(f"⚠️  You're only getting {avg_sleep:.1f} hours of sleep. Try to get at least 7-9 hours!")
        elif avg_sleep > 9:
            print(f"⚠️  You're sleeping {avg_sleep:.1f} hours. That might be too much!")
        else:
            print(f"✓ Great job! {avg_sleep:.1f} hours of sleep is healthy.")
        
        # Calorie advice
        if avg_calories < 1500:
            print(f"⚠️  You're only eating {avg_calories:.0f} calories. You might need more energy!")
        elif avg_calories > 3000:
            print(f"⚠️  You're eating {avg_calories:.0f} calories. Consider reducing your intake.")
        else:
            print(f"✓ Good! {avg_calories:.0f} calories is a reasonable amount.")
        
        print("-" * 40)


def main():
    people = []
    
    while True:
        print("\n=== Health Tracking System ===")
        print("1. Create new person")
        print("2. Add sleep data")
        print("3. Add calorie data")
        print("4. View health report")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter person's name: ")
            person = Person(name)
            people.append(person)
            print(f"✓ {name} has been added!")
        
        elif choice == "2":
            if len(people) == 0:
                print("❌ No people created yet. Create a person first!")
                continue
            
            print("\nAvailable people:")
            for i, p in enumerate(people):
                print(f"{i + 1}. {p.name}")
            
            try:
                person_num = int(input("Select person number: ")) - 1
                if 0 <= person_num < len(people):
                    hours = float(input("Enter hours of sleep: "))
                    people[person_num].add_sleep(hours)
                    print(f"✓ Sleep data added for {people[person_num].name}")
                else:
                    print("❌ Invalid person number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "3":
            if len(people) == 0:
                print("❌ No people created yet. Create a person first!")
                continue
            
            print("\nAvailable people:")
            for i, p in enumerate(people):
                print(f"{i + 1}. {p.name}")
            
            try:
                person_num = int(input("Select person number: ")) - 1
                if 0 <= person_num < len(people):
                    calories = float(input("Enter calories consumed: "))
                    people[person_num].add_calories(calories)
                    print(f"✓ Calorie data added for {people[person_num].name}")
                else:
                    print("❌ Invalid person number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "4":
            if len(people) == 0:
                print("❌ No people created yet. Create a person first!")
                continue
            
            print("\nAvailable people:")
            for i, p in enumerate(people):
                print(f"{i + 1}. {p.name}")
            
            try:
                person_num = int(input("Select person number: ")) - 1
                if 0 <= person_num < len(people):
                    people[person_num].give_health_advice()
                else:
                    print("❌ Invalid person number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "5":
            print("Goodbye! Stay healthy! 👋")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()