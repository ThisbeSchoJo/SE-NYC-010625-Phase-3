#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Hotel
from classes.many_to_many import Customer
from classes.many_to_many import Review

if __name__ == '__main__':
    # don't remove this line, it's for debugging!

    # Hotels
    marriott = Hotel("Marriott")
    the_chanler_at_cliff_walk = Hotel("Chanler Hotel")

    # Customers
    alice_baker = Customer("Alice", "Baker")
    bob_carris = Customer("Bob", "Carris")

    #Reviews
    review_1 = Review(marriott, bob_carris, 4, "Pretty awesome amenities here!")
    review_2 = Review(the_chanler_at_cliff_walk, bob_carris, 5, "Best hotel ever!")
    review_3 = Review(marriott, bob_carris, 3, "Not as good as my first experience.")
    review_4 = Review(marriott, alice_baker, 1, "Found bed bugs...")


    ipdb.set_trace()