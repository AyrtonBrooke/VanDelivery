import datetime

# Define the start and end times for the delivery schedule
start_time = datetime.time(hour=6)
end_time = datetime.time(hour=22)

delivery_schedule = {
    "Monday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "2 Oak St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [5],
            },
        ]
    },
    "Tuesday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "time": 15,
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "time": 8,
                "boxes": [3],
            },
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [1],
            },
        ]
    },
    "Wednesday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "2 Oak St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "time": 8,
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [3],
            },
        ]
    },
    "Thursday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [1],
            },
        ]
    },
    "Friday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [1],
            },
        ]
    },
    "Saturday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [1],
            },
        ]
    },
    "Sunday": {
        "start_time": start_time,
        "end_time": end_time,
        "deliveries": [
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "10 Pine St.",
                "location": {
                    "x": 1,
                    "y": 2
                },
                "boxes": [1],
            },
            {
                "address": "456 Oak St.",
                "location": {
                    "x": 2,
                    "y": 2
                },
                "boxes": [2],
            },
            {
                "address": "123 Main St.",
                "location": {
                    "x": 1,
                    "y": 1
                },
                "boxes": [3],
            },
            {
                "address": "789 Elm St.",
                "location": {
                    "x": 4,
                    "y": 1
                },
                "boxes": [1],
            },
        ]
    },
}
