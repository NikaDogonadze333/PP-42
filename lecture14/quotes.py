def save_quote():
  writer_name = input("შეიყვანეთ მწერალი: ")
  quote_text = input("შეიყვანეთ ციტატა: ")
  with open("quotes.txt", "w", encoding="utf-8") as file:
    file.write(f"Writer: {writer_name}\nQuote: {quote_text}\n")


def read_quotes():
  with open("quotes.txt", "r", encoding="utf-8") as file:
    print(file.read())