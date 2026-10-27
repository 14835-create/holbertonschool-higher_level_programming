#!/usr/bin/python3
"""Fetch json"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch and print post titles"""
    resp = requests.get(
            "https://jsonplaceholder.typicode.com/posts"
        )

    print("Status Code:", resp.status_code)

    if resp.status_code == 200:
        posts = resp.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and daves to posts.csv."""
    resp = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if resp.status_code == 200:
        posts = resp.json()

        with open(
            "posts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
