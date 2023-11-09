# ------ TASK 1 ------

# DECLARE journey_index : INTEGER //for FOR loop
departure_times = ["09:00", "11:00", "13:00", "15:00"]  # ARRAY STRING
departure_seats = [480, 480, 480, 480]  # ARRAY INTEGER
departure_passengers = [0, 0, 0, 0]  # ARRAY INTEGER
departure_money_total = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL

return_times = ["10:00", "12:00", "14:00", "16:00"]  # ARRAY STRING
return_seats = [480, 480, 480, 640]  # ARRAY INTEGER
return_passengers = [0, 0, 0, 0]  # ARRAY INTEGER
return_money_total = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL


def display_screen():  # DECLARING PROCEDURE
    print("\n\t>>>>>>>     TRAIN JOURNEY DISPLAY     <<<<<<<\n")
    for journey_index in range(0, 4):
        if departure_seats[journey_index] != 0:
            print(
                "Journey No:",
                journey_index + 1,
                "| Departure Hour:",
                departure_times[journey_index],
                "\t| Tickets available:",
                departure_seats[journey_index],
            )
        else:
            print(
                "Journey No:",
                journey_index + 1,
                "| Departure Hour:",
                departure_times[journey_index],
                "\t| Closed!",
            )

        if return_seats[journey_index] != 0:
            print(
                "Journey No:",
                journey_index + 1,
                "| Return Hour:",
                return_times[journey_index],
                "\t| Tickets available:",
                return_seats[journey_index],
            )
        else:
            print(
                "Journey No:",
                journey_index + 1,
                "| Return Hour:",
                return_times[journey_index],
                "\t| Closed!",
            )
        print()
        print("-----------------------\n")


# ENDPROCEDURE

display_screen()  # CALL PROCEDURE

# ----------- TASK 2 -----------
num_of_passengers = up_trip = down_trip = free_tickets = 0  # INTEGER
one_way_ticket = 25.0  # CONSTANT
one_way_cost = 0.0  # REAL
# DECLARE num_index : INTEGER //for FOR loops


choice = input("Do you want to buy ticket(s)? Enter Yes or No: ")
while choice != "Yes" and choice != "No":
    choice = input("Invalid Input! Enter Yes or No: ")

while choice != "No":
    print("\n-----------------------\n")
    #
    up_trip = int(input("Enter Journey number for your chosen departure hour: ")) - 1
    while up_trip not in range(0, 4):
        up_trip = int(input("Error! Enter Journey number from (1, 2, 3, 4): ")) - 1
    #
    print("\n----- Return Hours Available -----\n")
    for num_index in range(up_trip, 4):
        print(
            "Journey No:",
            num_index + 1,
            " | Return Hour:",
            return_times[num_index],
            " | Remaining Tickets:",
            return_seats[num_index],
        )
    print()
    down_trip = int(input("Enter Journey number for your chosen Return hour: ")) - 1
    while down_trip < up_trip or down_trip > 3:
        down_trip = (
            int(input("Error! Enter Journey number from the given list above: ")) - 1
        )
    #
    print()
    num_of_passengers = int(input("Enter number of passengers for trip: "))
    while num_of_passengers <= 0:
        num_of_passengers = int(input("Error! Enter number greater than 0: "))

    if (
        num_of_passengers > departure_seats[up_trip]
        or num_of_passengers > return_seats[down_trip]
    ):
        print("\n####################\n")
        print("Seats not available for chosen hours")
        print("Please check the display below for available Seats =>")

    else:
        print("\n//// Seats Booked ////")
        if 10 <= num_of_passengers <= 80:
            free_tickets = num_of_passengers // 10
        else:
            free_tickets = 0
        one_way_cost = (num_of_passengers - free_tickets) * one_way_ticket
        print("Total price for two-way journey: $", one_way_cost * 2, sep="")
        #
        departure_passengers[up_trip] += num_of_passengers
        departure_seats[up_trip] -= num_of_passengers
        departure_money_total[up_trip] += one_way_cost
        #
        return_passengers[down_trip] += num_of_passengers
        return_seats[down_trip] -= num_of_passengers
        return_money_total[down_trip] += one_way_cost

    display_screen()  # CALL PROCEDURE
    print("Do you want to buy ticket(s)? Enter Yes or No")
    choice = input()
    while choice != "Yes" and choice != "No":
        choice = input("Invalid Input! Enter Yes or No: ")

# ----------- TASK 3 -----------
total_amount = 0.0  # INTEGER (FOR TASK 3)
total_passengers = 0  # INTEGER
max_train = ""  # STRING (Empty)
most_passengers = 0  # INTEGER
# DECLARE count_index : INTEGER //for FOR loops

print("\n")
print(" ------ END OF THE DAY ------ ")
print("\n")
for count_index in range(0, 4):
    print(
        "Journey No:",
        count_index + 1,
        "\t| Departure Hour:",
        departure_times[count_index],
        "\t| Number of passengers:",
        departure_passengers[count_index],
        "\t| Total money: $",
        departure_money_total[count_index],
        sep="",
    )
    print(
        "Journey No:",
        count_index + 1,
        "\t| Return Hour:",
        return_times[count_index],
        "\t| Number of passengers:",
        return_passengers[count_index],
        "\t| Total money: $",
        return_money_total[count_index],
        sep="",
    )
    print("\n-----------------------\n")

for index_count in range(0, 4):
    total_passengers += departure_passengers[index_count]
    total_amount += (departure_money_total[index_count] * 2)
for counti in range(0, 4):
    if departure_passengers[counti] > most_passengers:
        most_passengers = departure_passengers[counti]
        max_train = departure_times[counti]
    if return_passengers[counti] > most_passengers:
        most_passengers = return_passengers[counti]
        max_train = return_times[counti]

print("Total money earned today: $", total_amount, sep="")
print("Total passengers travelled today:", total_passengers)
print("The train journey with the highest number of passengers today:", max_train)
input("Press Enter to Exit!")
