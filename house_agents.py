# File: house_agent.py
# A simple program with classes representing info for house agent


class Property:
    """
    Representing some common info for property
    """
    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        """
        (str) -> None
        Initialize the new property and add the num of square feet, beds, baths
        :param square_feet: str
        :param beds: str
        :param baths: str
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Display the info about property - the num of square feet, beds and bath
        """
        print("PROPERTY DETAILS")
        print("="*15)
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for object. Static method which get the num of
        square feet, beds and baths
        :return: dict of parameters
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))


class Apartment(Property):
    """
    Representing some common info for apartment. Have the same arg
    that property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony="", laundry="", **kwargs):
        """
        (str) -> None
        Initialize the new apartment and add the info about balcony and laundry
        :param balcony: str
        :param laundry: str
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Display the info about apartment - about laundry and balcony
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for object. Static method which get the info
        about laundry and balcony in the apartment
        :return: dict of parameters
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property "
                                  "have? ", Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init


class House(Property):
    """
    Representing some common info for house. Have the same arg
    that property
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        (str) -> None
        Initialize the new house and add the info about the num of stories in
        the house, garage, if the house is fenced
        :param num_stories: str
        :param garage: str
        :param fenced: str
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Display the info about house - num of stories, garages and if the house
        is fenced
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for object. Static method which get the info
        about the num of stories, garage and if the house is fenced
        :return: dict of parameters
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced,
                            "garage": garage,
                            "num_stories": num_stories})
        return parent_init


class Purchase:
    """
    Representing some info about property that will be purchased
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        (str) -> None
        Initialize the new property that will be purchased and add the price
        and the amount of taxes
        :param price: str
        :param taxes: str
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Display the info about property that will be purchased - the price and
        the taxes
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for object that will be purchased. Static method
        which get the info about price and taxes
        :return: dict of parameters
                """
        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))


class Rental:
    """"
    Representing the info about property that will be rent
    """
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        """
        (str) -> None
        Initialize the property that will be rent and add the info about
        furnishing, utilities and rent
        :param furnished: str
        :param utilities: str
        :param rent: str
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Display the info about property that will be rent - the rent, utilities
        and furnishing
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for object that will be rent. Static method
        which get the info about the price rent, utilities and if the
        property is furnished
        :return: dict of parameters
        """
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated utilities? "),
                    furnished=get_valid_input("Is the property furnished? ",
                                              ("yes", "no")))


class HouseRental(Rental, House):
    """
    Representing the house that will be rent
    """
    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for house that will be rent. Static method
        which get all info
        :return: dict of parameters
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class HousePurchase(Purchase, House):
    """
    Representing the house that will be purchased
    """
    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for house that will be purchased. Static method
        which get all info
        :return: dict of parameters
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class ApartmentRental(Rental, Apartment):
    """
    Representing the apartment that will be rent
    """
    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for apartment that will be rent. Static method
        which get all info
        :return: dict of parameters
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    """
    Representing the apartment that will be purchased
    """
    @staticmethod
    def prompt_init():
        """
        () -> dict
        Get the necessary info for apartment that will be purchased.
        Static method which get all info
        :return: dict of parameters
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


def get_valid_input(input_string, valid_options):
    """
    (str, tuple) -> str
    the function built a request for user and get the response from the exact
    given parameters - valid options
    return the response from user
    :param input_string: str
    :param valid_options: tuple of valid str
    :return: str
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Agent:
    """
    Representing the Agent with the list of his properties
    """
    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase}

    def __init__(self):
        """
        Initialize the new agent with his list of property
        """
        self.property_list = []

    def display_properties(self):
        """
        Display all info about every apartment or house in agent's list of
        properties
        """
        for properties in self.property_list:
            properties.display()

    def add_property(self):
        """
        the function get the info about the type of property which should be
        added to the list, indicates that type and add the object with all
        parameters to the list
        """
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
