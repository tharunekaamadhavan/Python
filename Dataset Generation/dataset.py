import csv
import random
import faker
from datetime import datetime, timedelta
from datetime import timedelta

# Initialize Faker library to generate fake data
fake = faker.Faker()
def generate_fake_timestamp(start_date, end_date):
    timestamp = fake.date_time_between(start_date=start_date, end_date=end_date)
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

# Example start and end dates for timestamp range
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

# Function to generate a random price
def generate_price():
    return round(random.uniform(10.0, 100.0), 2)

# Function to generate a random quantity
def generate_quantity():
    return random.randint(10, 200)
def generate_time_spent():
    # Generate a random time duration between 1 second and 1 hour
    return random.randint(1, 3600)

# Generate and write 2000 records to a CSV file
with open('inventoryy.csv', 'w', newline='') as csvfile:
    fieldnames = ['Product ID', 'Product Name', 'Category', 'Price', 'Quantity', 'Supplier', 'Supplier Contact', 'Items', 'Timestamp', 'Interaction Count', 'Average Time Spent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(2000):
        interaction_count = random.randint(0, 1000)
        total_time_spent = sum(generate_time_spent() for _ in range(interaction_count))
        average_time_spent = total_time_spent / (interaction_count + 1) if interaction_count > 0 else 0

        writer.writerow({
            'Product ID': fake.random_int(min=1000, max=9999),
            'Product Name': fake.word(),
            'Category': random.choice(['Men\'s Clothing', 'Men\'s Shoes', 'Men\'s Accessories', 'Women\'s Clothing', 'Women\'s Shoes', 'Women\'s Accessories']),
            'Price': generate_price(),
            'Quantity': generate_quantity(),
            'Supplier': fake.company(),
            'Supplier Contact': fake.email(),
            'Items':random.choice(["Pant & shirt","Formal Shoe","Wrist Watch","Leggins","Shoes","Bracelet"]),
            'Timestamp': generate_fake_timestamp(start_date, end_date),
            'Interaction Count': random.randint(0, 1000),
        })

print("Dataset generated successfully.")
