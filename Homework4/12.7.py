# George Tannous 1971969
# 12.7

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    max_heart_rate = 220
    fat_burning_rate = 0.7
    heart_rate = (max_heart_rate - age) * fat_burning_rate
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as e:
        print(f"{e}\nCould not calculate heart rate info.\n")

