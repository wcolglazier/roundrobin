def generate_schedule(teams, repetitions):
    n = len(teams)
    base_schedule = []

    # If odd number of teams, add a "Bye" team
    if n % 2 != 0:
        teams.append("Bye")
        n += 1

    for i in range(n - 1):
        round_games = []
        for j in range(n // 2):
            round_games.append((teams[j], teams[n - j - 1]))
        base_schedule.append(round_games)

        # Rotate the teams for the next round
        teams.insert(1, teams.pop())

    # Repeat the base_schedule according to the specified repetitions
    full_schedule = []
    for _ in range(repetitions):
        full_schedule.extend(base_schedule)

    return full_schedule

def main():
    # Get the teams from the user in a single line
    teams_input = input("Enter team names separated by commas: ")
    teams = [team.strip() for team in teams_input.split(",")]

    # Get the number of times each team plays against each other
    repetitions = int(input("How many times should each team play against each other? "))

    # Generate the schedule
    schedule = generate_schedule(teams, repetitions)

    # Print the schedule
    print("\nGame Schedule:")
    round_counter = 1
    for round_games in schedule:
        print(f"Round {round_counter}:")
        for game in round_games:
            if "Bye" not in game:  # Do not display games involving "Bye"
                print(f"Game: {game[0]} vs {game[1]}")
        round_counter += 1

    # Print total number of games
    total_games = sum([len(round) for round in schedule]) - schedule.count(('Bye',))  # Exclude games involving "Bye"
    print(f"\nTotal number of games to be played: {total_games}")

if __name__ == "__main__":
    main()
