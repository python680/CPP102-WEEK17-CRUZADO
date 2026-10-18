def get_initial_readings():
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    return text.isdigit()


def add_reading(readings):
    text = input("Enter new reading: ").strip()

    if text == "":
        print("\nInvalid input. The reading cannot be empty.")
        return

    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return

    value = int(text)

    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return

    readings.append(value)
    print("\nReading added successfully.")


def classify_reading(reading, warning_limit=30, critical_limit=35):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    return "CRITICAL"


def compute_total(readings):
    total = 0
    for reading in readings:
        total += reading
    return total


def compute_average(readings):
    if not readings:
        return 0.0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    if not readings:
        return 0

    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    if not readings:
        return 0

    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    count = 0
    for reading in readings:
        if classify_reading(
            reading, warning_limit, critical_limit
        ) == category:
            count += 1
    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    return "NORMAL"


def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")
    for index, reading in enumerate(readings, start=1):
        print(f"Reading {index}: {reading} °C")


def display_classifications(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading, 30, 35)}")


def display_summary(readings):
    number = len(readings)

    if number == 0:
        print("\nNo readings available.")
        return

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_count / number * 100:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_count / number * 100:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_count / number * 100:.2f}%)")
    print()
    print("Overall Status: " +
          determine_overall_status(warning_count, critical_count))


def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    readings = get_initial_readings()

    while True:
        display_menu()

        try:
            choice = input("\nEnter choice: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram stopped. Thank you for using the Device Monitoring System.")
            break

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            try:
                add_reading(readings)
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()


