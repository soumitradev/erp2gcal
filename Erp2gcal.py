import datetime as dt


def fileParse(text):
    contents = []
    sentences_to_miss = [
        "This Week's Schedule",
        "    Class   Schedule",
        "Academic Calendar Deadlines",
        "",
    ]
    with open(text, "r") as f:
        for item in f.read().split("\n"):
            if item not in sentences_to_miss:
                contents.append(item)
    return contents


class Course:
    def __init__(self, name, typ, room, days, start):
        self.name = name
        self.typ = typ
        self.days = days
        self.start = start
        self.end = None
        self.room = room

    def day(self):
        days = []
        dayDict = {
            "Mo": "Monday",
            "Tu": "Tuesday",
            "We": "Wednesday",
            "Th": "Thursday",
            "Fr": "Friday",
            "Sa": "Saturday",
        }

        for i in range(0, len(self.days), 2):
            # days.append(dayDict[self.days[i : i + 2]])
            days.append(self.days[i : i + 2].upper())
        return days

    def timings(self):
        tdelta = {
            "TUT": dt.timedelta(hours=1),
            "LAB": dt.timedelta(hours=2),
            "TUT": dt.timedelta(hours=1),
        }


def coursesGen(courses_info):
    courses = []
    for i in range(0, len(courses_info), 4):

        courses.append(
            Course(
                courses_info[i],
                courses_info[i + 1].split()[0],
                courses_info[i + 3].split()[1],
                courses_info[i + 2].split()[0],
                courses_info[i + 2].split()[1],
            )
        )

    return courses


def timeGen(string):
    hour = string.split(":")[0]  # ['2', '00PM']
    meridian = string.split(":")[1][2:]  #'00PM' -> PM


def main():
    filecont = fileParse("text.txt")
    courses = coursesGen(filecont)
    return courses


main()
