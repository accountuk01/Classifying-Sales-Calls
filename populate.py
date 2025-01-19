import os
import sys
import argparse
from datetime import datetime
from collections import defaultdict
import subprocess


def get_file_date(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path)).date()


def group_files_by_date(directory):
    # I decided to group files edited on the same day in a single commit:
    grouped_files = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("."):
                continue
            file_path = os.path.join(root, file)
            # I added this hack to skip the .git directory
            if ".git" in file_path:
                continue
            file_date = get_file_date(file_path)
            grouped_files[file_date].append(file_path)
    return grouped_files


def commit_files(files, date, author, author_email):
    print(files)
    for file in files:
        subprocess.run(["git", "add", file], check=True)

    commit_date = date.strftime("%Y-%m-%d 00:00:00")
    commit_message = f"Adding files from {date}"

    env = os.environ.copy()
    # Here'This is the most important bit: these environment variables are used
    # by Git to set the author and committer dates and names
    env["GIT_AUTHOR_DATE"] = commit_date
    env["GIT_COMMITTER_DATE"] = commit_date
    env["GIT_AUTHOR_NAME"] = author
    env["GIT_AUTHOR_EMAIL"] = author_email
    env["GIT_COMMITTER_NAME"] = author
    env["GIT_COMMITTER_EMAIL"] = author_email

    result = subprocess.run(
        ["git", "commit", "-m", commit_message],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )

    commit_hash = result.stdout.split()[1]
    return commit_hash


def main():
    parser = argparse.ArgumentParser(
        description="Populate Git repo with historical commits"
    )
    parser.add_argument("directory", help="Directory containing the files")
    parser.add_argument("--author", required=True, help="Author of the commits")
    # I added this option by hand:
    parser.add_argument("--email", required=True, help="Email of author")
    args = parser.parse_args()

    os.chdir(args.directory)

    if not os.path.exists(".git"):
        print(
            "Error: No .git directory found. Please initialize a Git repository first."
        )
        sys.exit(1)

    grouped_files = group_files_by_date(args.directory)

    for date, files in sorted(grouped_files.items()):
        commit_hash = commit_files(files, date, args.author, args.email)
        print(f"Commit: {commit_hash}, Date: {date}")


if __name__ == "__main__":
    main()
