import time

devices = ["iphone", "android", "radio", "tv", "tablet", "pc", "laptop"] * (10 ** 9 // 7)


def check_device(device_name):
    start_time = time.time()
    is_present = device_name in devices
    end_time = time.time()

    time_taken = end_time - start_time

    # Print results
    if is_present:
        print(f"{device_name} is in the list.")
    else:
        print(f"{device_name} is NOT in the list.")

    print(f"Time taken: {time_taken:.6f} seconds")


user_input = input("Enter the device name to search for: ")

check_device(user_input)