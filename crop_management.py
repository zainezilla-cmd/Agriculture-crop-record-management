
"""
Agriculture Crop Record Management System

Purpose:
To manage crop records using Object-Oriented Programming.
"""


class Crop:
    """Represents one crop record."""

    # Class attribute shared by all Crop objects
    total_crops = 0

    def __init__(self, crop_id, name, quantity):
        """Create a crop with its ID, name and harvest quantity."""
        self.crop_id = crop_id
        self.name = name
        self.quantity = quantity

        Crop.total_crops += 1

    # Instance method
    def display_info(self):
        """Display information about this crop."""
        print("-" * 35)
        print("Crop ID:", self.crop_id)
        print("Crop Name:", self.name)
        print("Harvest Quantity:", self.quantity, "kg")
        print("-" * 35)

    # Instance method
    def update_quantity(self, new_quantity):
        """Update this crop's harvest quantity."""
        if Crop.is_valid_quantity(new_quantity):
            self.quantity = new_quantity
            return True

        return False

    # Class method
    @classmethod
    def get_total_crops(cls):
        """Return the number of Crop objects created."""
        return cls.total_crops

    # Static method
    @staticmethod
    def is_valid_quantity(quantity):
        """Check that a harvest quantity is not negative."""
        return quantity >= 0


class Farm:
    """Manages a collection of crop records."""

    def __init__(self):
        # A list stores the Crop objects
        self.crops = []

    def find_crop(self, crop_id):
        """Find a crop using its ID."""
        for crop in self.crops:
            if crop.crop_id.lower() == crop_id.lower():
                return crop

        return None

    def add_crop(self, crop):
        """Add a crop if its ID is unique."""
        if self.find_crop(crop.crop_id) is not None:
            return False

        self.crops.append(crop)
        return True

    def display_all_crops(self):
        """Display every registered crop."""
        if not self.crops:
            print("No crop records have been registered.")
            return

        for crop in self.crops:
            crop.display_info()

    def update_crop(self, crop_id, new_quantity):
        """Find a crop and update its quantity."""
        crop = self.find_crop(crop_id)

        if crop is None:
            return False, "Crop ID not found."

        if not Crop.is_valid_quantity(new_quantity):
            return False, "Quantity cannot be negative."

        crop.update_quantity(new_quantity)
        return True, "Crop quantity updated successfully."


def read_quantity(prompt):
    """Read a valid, non-negative quantity from the user."""
    while True:
        try:
            quantity = float(input(prompt))

            if Crop.is_valid_quantity(quantity):
                return quantity

            print("Quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid number, such as 25 or 12.5.")


def main():
    """Run the crop management menu."""
    farm = Farm()

    while True:
        print("\n===================================")
        print(" AGRICULTURE CROP MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add a crop")
        print("2. Display all crops")
        print("3. Search for a crop")
        print("4. Update crop quantity")
        print("5. Count registered crop records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            crop_id = input("Enter crop ID: ").strip()
            name = input("Enter crop name: ").strip()

            if not crop_id or not name:
                print("Crop ID and name cannot be empty.")
                continue

            # Check the ID before creating the object
            if farm.find_crop(crop_id) is not None:
                print("That crop ID already exists.")
                continue

            quantity = read_quantity(
                "Enter harvest quantity in kg: "
            )

            crop = Crop(crop_id, name, quantity)

            if farm.add_crop(crop):
                print("Crop registered successfully!")

        elif choice == "2":
            farm.display_all_crops()

        elif choice == "3":
            crop_id = input("Enter the crop ID to search for: ").strip()
            crop = farm.find_crop(crop_id)

            if crop is not None:
                crop.display_info()
            else:
                print("Crop ID not found.")

        elif choice == "4":
            crop_id = input("Enter the crop ID to update: ").strip()

            new_quantity = read_quantity(
                "Enter the new harvest quantity in kg: "
            )

            success, message = farm.update_crop(
                crop_id, new_quantity
            )

            print(message)

        elif choice == "5":
            print(
                "Total registered crop records:",
                len(farm.crops)
            )
            print(
                "Total Crop objects created:",
                Crop.get_total_crops()
            )

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
