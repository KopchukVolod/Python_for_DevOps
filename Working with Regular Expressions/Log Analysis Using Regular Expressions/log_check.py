#!/usr/bin/env python3

import re
import csv

# Ініціалізуємо словники для підрахунку повідомлень про помилки та статистики користувачів
error_messages = {}
user_statistics = {}

# Функція для обробки повідомлень про помилки
def process_error_message(line):
    pattern = r"ERROR (\w+)"
    result = re.search(pattern, line)
    if result:
        error = result.group(1)
        if error in error_messages:
            error_messages[error] += 1
        else:
            error_messages[error] = 1

# Функція для обробки повідомлень користувачів
def process_user_message(line):
    pattern = r"\((\w+)\)"
    result = re.search(pattern, line)
    if result:
        user = result.group(1)
        if user in user_statistics:
            if "INFO" in line:
                user_statistics[user]["INFO"] += 1
            elif "ERROR" in line:
                user_statistics[user]["ERROR"] += 1
        else:
            user_statistics[user] = {"INFO": 0, "ERROR": 0}
            if "INFO" in line:
                user_statistics[user]["INFO"] += 1
            elif "ERROR" in line:
                user_statistics[user]["ERROR"] += 1

# Відкриваємо файл syslog.log для читання
with open("syslog.log", "r") as file:
    for line in file:
        process_error_message(line)
        process_user_message(line)

# Сортуємо словники перед створенням CSV-звітів
sorted_errors = sorted(error_messages.items(), key=lambda x: x[1], reverse=True)
sorted_users = sorted(user_statistics.items(), key=lambda x: x[0])

# Створюємо звіт про повідомлення про помилки
with open("error_message.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    writer.writerows(sorted_errors)

# Створюємо звіт про статистику користувачів
with open("user_statistics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for user, stats in sorted_users:
        writer.writerow([user, stats["INFO"], stats["ERROR"]])
