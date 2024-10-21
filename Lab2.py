def display_main_menu():
    print("===== Temperature Processing Program =====")
    print("1. Enter temperatures")
    print("2. Calculate average temperature")
    print("3. Find minimum and maximum temperature")
    print("4. Sort temperatures")
    print("5. Calculate median temperature")
    print("=========================================")



def get_user_input():
    temp_list = []
    while True:
        try:
            temp = float(input("Enter a temperature (or 'done' to finish): "))
            temp_list.append(temp)
        except ValueError:
            # If user enters 'done', break the loop
            break
    return temp_list


def calc_average(temp_list):
    if len(temp_list) == 0:
        return 0.0  # Avoid division by zero
    return sum(temp_list) / len(temp_list)


def find_min_max(temp_list):
    if len(temp_list) == 0:
        return [0.0, 0.0]  # Handle empty list
    return [min(temp_list), max(temp_list)]


def sort_temperature(temp_list):
    return sorted(temp_list)


def calc_median_temperature(temp_list):
    if len(temp_list) == 0:
        return 0.0  # Handle empty list
    sorted_list = sort_temperature(temp_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2  # Even number of elements
    else:
        return sorted_list[mid]  # Odd number of elements


def main():
    print('Enter your name:')
    name = input()
    print('Hello, ' + name)

    display_main_menu()
    temp_list = get_user_input()

    average = calc_average(temp_list)
    print(f"Average Temperature: {average:.2f}")

    min_max = find_min_max(temp_list)
    print(f"Min Temperature: {min_max[0]}, Max Temperature: {min_max[1]}")

    sorted_temps = sort_temperature(temp_list)
    print(f"Sorted Temperatures: {sorted_temps}")

    median = calc_median_temperature(temp_list)
    print(f"Median Temperature: {median}")

if __name__ == "__main__":
    main()
