def weekend(day):
    match day:
        case "saturday" | "sunday":
            return "it's a weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "it's not a weekend"
        case _:
            return "it's not a weekend"

print(weekend("saturday"))