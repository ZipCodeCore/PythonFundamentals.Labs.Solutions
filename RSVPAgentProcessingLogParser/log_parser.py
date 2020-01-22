import re

if __name__ == '__main__':
    print("WARNINGS:")
    with open('data/rsvp_agent_log.dat', 'r') as file:
        for line in file:
            for match in re.finditer(r"(\d{2}/\d{2}\s\d{2}:\d{2}:\d{2})\s(WARNING):[\.a-z_]*:\s(.*)$", line):
                print(f"{match.group(1)} -- {match.group(3)}")
