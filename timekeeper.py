#! /usr/bin/env python3
import icalendar as ical
import datetime as dt
import pytz
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "name",
    nargs="+",
    help="name the event to timekeep")
parser.add_argument(
    "--startevent",
    help="start a new event",
    action="store_true")
parser.add_argument(
    "--stopevent",
    help="stop an ongoing event",
    action="store_true")
parser.add_argument(
    "--dir",
    help="where to look for / store the .ics file",
    default="/home/patrick/.cache/timekeeper/")

args = parser.parse_args()

if (args.startevent):
    print("starting event")

    n = dt.datetime.now()
    dtstart = n - dt.timedelta(
        seconds=n.second, minutes=round(n.minute % 15)
    )

    try:
        with open(args.dir + "/" + n.strftime("%Y%m%d") + ".ics", "rb") as f:
            c = ical.Calendar.from_ical(f.read())
    except Exception:
        c = ical.Calendar()

    e = ical.Event()
    e.add("summary", " ".join(args.name))
    e.add("dtstart", pytz.timezone("Europe/Berlin").localize(dtstart))

    c.add_component(e)

    with open(args.dir + "/" + n.strftime("%Y%m%d") + ".ics", "wb") as f:
        f.write(c.to_ical())

if (args.stopevent):
    print("stopping event")
    n = dt.datetime.now()
    dtend = n - dt.timedelta(
        seconds=n.second, minutes=round(n.minute % 15)
    )

    try:
        with open(args.dir + "/" + n.strftime("%Y%m%d") + ".ics", "rb") as f:
            c = ical.Calendar.from_ical(f.read())


        e = c.walk("VEVENT")[-1]
        e["summary"] = " ".join(args.name)
        e.add("dtend", pytz.timezone("Europe/Berlin").localize(dtend))

        print(c.to_ical())

        with open(args.dir + "/" + n.strftime("%Y%m%d") + ".ics", "wb") as f:
            f.write(c.to_ical())

    except Exception:
        print(f"cant read from {args.dir}/{n.strftime('%Y%m%d')}.ics")
