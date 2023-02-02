import csv
import datetime

meteo = [
    (
        ("temperature", 42),
        ("date", datetime.date(2017, 1, 22)),
        ("locations", ("Berlin", "Paris")),
        ("weather", "sunny"),
    ),
    (
        ("temperature", -42),
        ("date", datetime.date(2017, 1, 22)),
        ("locations", ("Marseille", "Moscow")),
        ("weather", "cloudy"),
    ),
]


def generate_csv(a_list):
    with open("results.csv", "w", newline="") as csvfile:
        fieldnames = [[column[0] for column in block] for block in a_list]
        fieldnames = fieldnames[0] + fieldnames[1]
        fieldnames = list(dict.fromkeys(fieldnames))

        csv_out = csv.DictWriter(
            csvfile,
            delimiter=",",
            quoting=csv.QUOTE_MINIMAL,
            quotechar='"',
            fieldnames=fieldnames,
        )

        parsed_data = [dict(block) for block in a_list]

        # for key, value in a_list[0].items():
        #     if type(value) == tuple:
        #         a_list[key] = ' '.join(a_list[key])

        csv_out.writeheader()
        for line in parsed_data:
            csv_out.writerow(line)
        print(parsed_data)
        # # Parse headers
        # headers = [[column[0] for column in block] for block in a_list]
        # headers = headers[0] + headers[1]
        # headers = list(dict.fromkeys(headers))
        # csv_out.writerow(headers)

        # # Parse values
        # values = [[column[1] for column in block] for block in a_list]
        # for row in values:
        #     for index, item in enumerate(row):
        #         if type(item) == tuple:
        #             row[index] = str(row[index]).strip("'()").strip("'")
        #     csv_out.writerow(row)
    return


generate_csv(meteo)
