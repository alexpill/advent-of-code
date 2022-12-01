#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import time
import requests as rq

from datetime import datetime


def error(msg):
    print(f"Error: {msg}")
    exit(1)


def fetch_input_values(session_cookie, out_file, day, year):
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = rq.get(input_url, cookies={"session": session_cookie})
    if r.status_code != 200:
        error("Couldn't get the input")
    with open(f"{year}/{day}/{out_file}_input.txt", "w") as input_file:
        input_file.write(r.text)

def fetch_problem(day, year):
    input_url = f"https://adventofcode.com/{year}/day/{day}"
    r = rq.get(input_url)
    if r.status_code != 200:
        error("Couldn't get the problem")
    else:
        time.sleep(1)
        return r.text

def fetch_problem_name(problem):
    pn = problem.split("---")[1].split(":")[1].strip().lower().replace(" ", "_")
    return pn

def main():
    current_date = datetime.now()
    parser = argparse.ArgumentParser(description=
            "Generate skeleton for the given day and year of advent of code")
    parser.add_argument("day", type=int, default=current_date.day, nargs="?",
                        help=f"Day of the advent of code "
                             f"(default: {current_date.day})")
    parser.add_argument("year", type=int, default=current_date.year, nargs="?",
                        help=f"Year of the advent of code "
                             f"(default: {current_date.year})")
    parser.add_argument("-session-cookie", type=str, default=None,
                        help="Session cookie to get the input")
    options = parser.parse_args()

    day = options.day
    year = options.year
    session_cookie = options.session_cookie

    if year > current_date.year or  \
        year == current_date.year and day > current_date.day:
        error("You can't go in the future!")
    if not os.path.exists(f"{year}/{day}"):
        os.makedirs(f"{year}/{day}")

    problem = fetch_problem(day, year)
    problem_name = fetch_problem_name(problem)

    if session_cookie is not None:
        fetch_input_values(session_cookie, problem_name, day, year)

    with open("template", "r") as template:
        with open(f"{year}/{day}/{problem_name}.py", "w") as out:
            out.write(template.read())

if __name__ == "__main__":
    main()
