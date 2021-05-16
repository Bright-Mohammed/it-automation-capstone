#!/usr/bin/env python3

import json
import locale
import sys
import operator
import reports
import emails
import os


max_sale_model = {"model": "", "sale": 0}
car_year_sales = {}

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  for item in data:
    #car_data.append({item["id"]: format_car(item["car"])})
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if max_sale_model["sale"] < item["total_sales"]:
      max_sale_model["sale"] = item["total_sales"]
      max_sale_model["model"] = item["car"]["car_model"]
    # TODO: also handle most popular car_year
    car_year = str(item["car"]["car_year"])
    car_year_sales[car_year] = car_year_sales.get(car_year, 0) + item["total_sales"]
    
    
  sorted_cars = sorted(car_year_sales.items(), key=operator.itemgetter(1), reverse=True)
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sale_model["model"], max_sale_model["sale"]),
    "The most popular year was {} with {} sales.".format(sorted_cars[0][0], sorted_cars[0][1])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = "<br/>".join(process_data(data))
  print(summary)
  # TODO: turn this into a PDF report
  table_data = cars_dict_to_table(data)
  reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruits", summary, table_data)
  # TODO: send the PDF report as an email attachment
  message = emails.generate("automation@example.com", "{}@example.com".format(os.environ.get('USER')), "Sales summary for last month", "\n".join(process_data(data)), "/tmp/email_report.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)