class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        MovieTicket.total_tickets_sold += 1

ticket1 = MovieTicket("Avatar 2", 12, 25)
ticket2 = MovieTicket("Inception", 5, 20)
ticket3 = MovieTicket("Interstellar", 18, 22)

print(f"კინოთეატრი: {ticket1.cinema_name} | ფილმი: {ticket1.movie_title} | ადგილი: {ticket1.seat_number} | ფასი: {ticket1.price} ლარი")
print(f"კინოთეატრი: {ticket2.cinema_name} | ფილმი: {ticket2.movie_title} | ადგილი: {ticket2.seat_number} | ფასი: {ticket2.price} ლარი")
print(f"კინოთეატრი: {ticket3.cinema_name} | ფილმი: {ticket3.movie_title} | ადგილი: {ticket3.seat_number} | ფასი: {ticket3.price} ლარი")

print(f"სულ გაყიდული ბილეთები: {MovieTicket.total_tickets_sold}")