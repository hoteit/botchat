from datetime import datetime
# !pip install parsedatetime
import parsedatetime as pdt


def dateparser(time_string):
    # "June 11th at 4:00 PM"
    cal = pdt.Calendar()
    now = datetime.now()
    gen_date = cal.parseDT(time_string, now)[0]
    new_date = gen_date.strftime('%B %#d= at %I:%M %p')
    day = int(gen_date.strftime('%#d'))

    # we need to find the suffix of the day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    # replace the '=' with the suffix
    new_date = new_date.replace('=', suffix)
    return new_date
