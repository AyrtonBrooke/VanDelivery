# import required modules
from delivery_schedule import delivery_schedule
import math
from typing import List, Tuple
from tabulate import tabulate


# define function to extract stops from a schedule for a given day
def get_stops_from_schedule(schedule: dict, day: str) -> List[tuple]:
    stops = []
    # loop over each delivery on the given day
    for delivery in schedule[day]["deliveries"]:
        # extract the location coordinates of the delivery and append to stops list
        stop = (delivery["location"]["x"], delivery["location"]["y"])
        stops.append(stop)
    return stops

# define function to calculate distance between two points in 2D space
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# define function to calculate time required to travel a given distance at a given speed
def calculate_delivery_time(distance, speed):
    time = distance / speed
    return time

# define function to calculate the optimal route to visit all stops in a given schedule for a day
def calculate_route(stops):
    # initialize current location of the van to (0, 0)
    current_location = (0, 0)
    # list to hold the route
    route = []
    # loop until all stops have been visited
    while stops:
        # find the closest stop to the current location
        closest_stop = min(stops, key=lambda s: distance(current_location[0], current_location[1], s[0], s[1]))
        # add the closest stop to the route
        route.append(closest_stop)
        # remove the closest stop from the list of stops
        stops.remove(closest_stop)
        # update the current location of the van
        current_location = closest_stop
    # add the starting point to the route
    route.append((0, 0))
    return route

# define function to sort deliveries in a schedule for a given day based on optimal route
def sort_deliveries_by_route(info):
    # Get the stops for the current day
    stops = [(d['location']['x'], d['location']['y']) for d in info['deliveries']]
    # Calculate the route for the day
    route = calculate_route(stops)
    # Sort the deliveries by their position in the route
    deliveries = info['deliveries']
    deliveries_sorted = []
    for r in route:
        for d in deliveries:
            if (d['location']['x'], d['location']['y']) == r:
                deliveries_sorted.append(d)
                break
    return deliveries_sorted

# define function to calculate time required to travel between two stops on a given route at a given speed
def calculate_time_to_next_stop(current_stop: Tuple[int, int], next_stop: Tuple[int, int], speed: int, route: List[Tuple[int, int]]) -> float:
    distance_per_stop = 0
    for i in range(len(route)):
        if route[i] == current_stop:
            for j in range(i+1, len(route)):
                if route[j] == next_stop:
                    distance_per_stop = sum([distance(route[k][0], route[k][1], route[k+1][0], route[k+1][1]) for k in range(i, j)])
                    break
            break
    time = distance_per_stop / speed
    return time * 60  # multiply time in hours by 60 to get time in minutes

def write_delivery_schedule(schedule: dict, filename: str):
    with open(filename, "w") as f:
        # Iterate over each day in the schedule
        for day, info in schedule.items():
            f.write(f"{day}:\n")
            start_time = info["start_time"]
            end_time = info["end_time"]

            # Sort the deliveries by their position in the route
            deliveries = sort_deliveries_by_route(info)

            # Print the stops for the current day
            stops = [(d['location']['x'], d['location']['y']) for d in deliveries] + [(0, 0)]
            f.write(f"Stops for {day}: {stops}\n\n")
            f.write("Good Morning Have a safe drive\n\n")

            # Calculate the route for the day
            route = calculate_route(stops)

            total_distance = 0
            total_time = 0
            for i in range(len(route)):
                current_stop = route[i]
                if i < len(route) - 1:
                    next_stop = route[i + 1]
                    stop_distance = distance(current_stop[0], current_stop[1], next_stop[0], next_stop[1])
                    time = calculate_time_to_next_stop(current_stop, next_stop, 30, route)
                else:
                    stop_distance = 0
                    time = 0
                total_distance += stop_distance
                total_time += time
                f.write(f"Location: ({current_stop[0]}, {current_stop[1]})\n")
                if i < len(route) - 1:
                    f.write(f"Next stop is {stop_distance:.2f} miles away and will take {time:.2f} minutes to get there.\n")
                else:
                    f.write("Welcome Back to HQ.\nThank you for completing all deliveries and returning safely to the headquarters!\n\n")

            # Print the total distance for the day
            f.write(f"Total distance for {day}: {total_distance:.1f} miles\n")
            f.write(f"Total time for {day}: {total_time:.2f} minutes\n\n")

            # Iterate over the sorted deliveries and print their information
            for i, delivery in enumerate(deliveries):
                f.write(f"Delivery {i + 1}:\n")
                f.write(f"Location: ({delivery['location']['x']}, {delivery['location']['y']})\n")
                f.write(f"Address: {delivery['address']}\n")
                f.write("Boxes to be delivered:\n")
                for boxes in delivery["boxes"]:
                    f.write(f"- {boxes}\n")
                f.write("\n")

def print_delivery_schedule_table(schedule: dict, filename: str):
    # Initialize a list to store the data for the table
    table_data = []

    # Iterate over each day in the schedule
    for day, info in schedule.items():
        start_time = info["start_time"]
        end_time = info["end_time"]

        # Sort the deliveries by their position in the route
        deliveries = sort_deliveries_by_route(info)

        # Calculate the stops for the current day
        stops = [(d['location']['x'], d['location']['y']) for d in deliveries] + [(0, 0)]

        # Calculate the route for the day
        route = calculate_route(stops)

        total_distance = 0
        total_time = 0
        for i in range(len(route)):
            current_stop = route[i]
            if i < len(route) - 1:
                next_stop = route[i + 1]
                stop_distance = distance(current_stop[0], current_stop[1], next_stop[0], next_stop[1])
                time = calculate_time_to_next_stop(current_stop, next_stop, 30, route)
            else:
                stop_distance = 0
                time = 0
            total_distance += stop_distance
            total_time += time

        # Add the information for the current day to the table data
        table_data.append([day, start_time, end_time, f"{total_distance:.1f}", f"{total_time:.2f}"])

    # Write the table to a txt file
    with open(filename, "w") as file:
        file.write(tabulate(table_data,
                            headers=["Day", "Start Time", "End Time", "Total Distance (miles)", "Total Time (minutes)"],
                            tablefmt="plain"))

    print(f"Delivery schedule table has been written to {filename}.\n")

# Print the updated delivery schedule
write_delivery_schedule(delivery_schedule, "delivery_schedule.txt")
print_delivery_schedule_table(delivery_schedule, "delivery_schedule_table.txt")
