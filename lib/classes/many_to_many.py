# Relationship: 1 Hotel has many customers and many reviews*
class Hotel:
    def __init__(self, name):
        self.name = name

    # "returns hotel's name" means you need a getter
    # "names must be" means you need a setter method 
    # (to check the value of the string and make sure it's in the range)
    # "should NOT be able to" means you need an attr**

    # not a getter decorator -- use a @property decorator
    @property
    def name_getter(self):
        return self._name
    
    # Have to reference the name of the getter with the setter
    @name_getter.setter
    def name(self, name_value):
        # isinstance bugs out with True (insinstance(True, int) returns True even though True isn't an int)
        # so type is better
        # if (not (type(name_value) == str)) or (len(name_value) > 20 or len(name_value) < 5):
        #     return
        # self._name = name_value
        if (type(name_value) == str) and ( 5 <= len(name_value) <=20):
            self._name = name_value
            # self.name = name_value would trigger it to recursively set the value in a loop*

    # Relationship: 1 Hotel has many Reviews (1-to-Many Relationship)
    def reviews(self):
        return [review for review in Review.all if review.hotel is self]

    # Relationship: 
    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
    
    def review_texts(self):
        if len(self.reviews()) == 0:
            return None
        else:
            return [review.text for review in self.reviews()]

    def average_rating(self):
        if len(self.reviews()) == 0:
            return None
        else:
            rating_list = [review.rating for review in self.reviews()]
            return sum(rating_list) / len(rating_list)
        
    # LAST DELIVERABLE ON CODE CHALLENGE SHOULD FOLLOW THIS FORMAT (HELPFUL TO SEPARATE INTO TWO FUNCTIONS)
    def customers_more_than_three_reviews(self):
        # returns a list of customers who have submitted more than 3 reviews for the hotel
        # customers must be of type Customer is already established below with property so don't need to do anything for that part here
        customer_list =  [customer for customer in self.customers() if self.has_more_than_3_reviews(customer)]

        if len(customer_list) == 0:
            return None
        else:
            return customer_list

    def has_more_than_3_reviews(self, customer):
        review_list = [review for review in customer.reviews() if review.hotel is self]
        if len(review_list) > 3:
            return True
        else:
            return False

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name_getter(self):
        return self._first_name
    
    @first_name_getter.setter
    def first_name(self, first_name_value):
        # check the type before you check the length because you can end up with a bug (don't want to check the length of something that is not a string)
        if (not hasattr(self, 'first_name') and (type(first_name_value) == str) and (len(first_name_value) > 0)):
            self._first_name = first_name_value

    @property
    def last_name_getter(self):
        return self._last_name
    
    @last_name_getter.setter
    def last_name(self, last_name_value):
        if (not hasattr(self, 'last_name') and (type(last_name_value) == str) and (len(last_name_value) > 0)):
            self._last_name = last_name_value

    # this is an instance method because 1 customer has many reviews (this is our association):
    # Relationship: 1 Customer has many reviews (1-to-Many Relationship):
    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    # Relationship: 1 Customer has many Hotels (through Reviews) (Many-to-Many Relationship):
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    # don't need any other customer info in the parameters bc we have the self
    def submit_review(self, hotel, rating, text):
        # self is the instance method of the Customer class...*
        # need to do it in the order that Review expects it (hotel, customer, rating, text)
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        return [hotel.name for hotel in self.hotels()]

    # def __repr__(self):
    #     return f"{Customer.first_name}"

# A review belongs to one customer and one hotel
class Review:

    all = []

    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text
        Review.all.append(self)

    @property
    def rating_getter(self):
        return self._rating
    
    @rating_getter.setter
    def rating(self, rating_value):
        if (not hasattr(self, 'rating') and (type(rating_value) == int) and ( 1 <= rating_value <= 5)):
            self._rating = rating_value

    @property
    def text_getter(self):
        return self._text
    
    @text_getter.setter
    def text(self, text_value):
        if (not hasattr(self, 'text') and (type(text_value) == str) and (3 <= len(text_value) <= 40)):
            self._text = text_value
    
    @property
    def hotel_getter(self):
        return self._hotel
    
    @hotel_getter.setter
    def hotel(self, hotel_value):
        # could also do isinstance()
        if type(hotel_value) == Hotel:
            self._hotel = hotel_value

    @property
    def customer_getter(self):
        return self._customer
    
    @customer_getter.setter
    def customer(self, customer_value):
        # coould also use type()
        if isinstance(customer_value, Customer):
            self._customer = customer_value
