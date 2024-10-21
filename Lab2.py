def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("get_user_input")
    return []  # Placeholder: This will eventually return a list of floats

def calc_average(temp_list):
    print("calc_average")
    return 0.0  # Placeholder: This will eventually return the average value

def find_min_max(temp_list):
    print("find_min_max")
    return [0.0, 0.0]  # Placeholder: This will eventually return [min_temp, max_temp]

def sort_temperature(temp_list):
    print("sort_temperature")
    return []  # Placeholder: This will eventually return a sorted list

def calc_median_temperature(temp_list):
    print("calc_median_temperature")
    return 0.0  # Placeholder: This will eventually return the median value

def main():
    display_main_menu()
    temp_list = get_user_input()
    average = calc_average(temp_list)
    min_max = find_min_max(temp_list)
    sorted_temps = sort_temperature(temp_list)
    median = calc_median_temperature(temp_list)

if __name__ == "__main__":
    main()
