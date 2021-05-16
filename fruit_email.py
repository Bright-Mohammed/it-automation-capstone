#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import os

desc_loc = "./supplier-data/descriptions"

def generate_summary():
  summary = []
  for file in os.listdir(desc_loc):
    d_filename = os.path.join(desc_loc, file)
    with open(d_filename, 'r') as f:
      name = f.readline().strip()
      weight = f.readline().strip()
      description = f.readline().strip()
      summary.append("name: {}\nweight: {}".format(name, weight))
  return summary

def generate(sender, recipient, subject):
  """Creates an email with an attachement."""
  # Basic Email formatting
  summary = generate_summary()
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content("\n\n".join(summary))
  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


if __name__ == "__main__":
  summary = generate("automation@example.com", "{}@example.com".format(os.environ.get('USER')), "Upload Completed - Online Fruit Store")
  send(summary)