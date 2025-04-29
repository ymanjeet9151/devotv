from faker import Faker
import random
import string
import time
from datetime import datetime, timedelta

fake = Faker('en_US')


def generate_email():
    """
    Generate fake Email using Faker Lib
    :return: snehil.mishra@impressico.com
    """
    return time.strftime('%m%d%y%H%M%S', time.localtime()) + fake.email()


def generate_first_name():
    """
    Generate fake First Name using Faker Lib
    :return: Automation
    """
    return fake.first_name()


def generate_middle_name():
    """
    Generate random Middle Name
    :return: P
    """
    return random.choice(string.ascii_uppercase)


def generate_last_name():
    """
    Generate fake Last Name using Faker Lib
    :return: QA
    """
    return fake.last_name()


def generate_state():
    """
    Select State using Random Lib
    :return: NY
    """
    state = ['NY', 'FL', 'MA', 'AZ', 'NJ', 'CA', 'LA', 'OH', 'WI', 'IL', 'AR', 'TX']
    return random.choice(state)


def generate_zip_code():
    """
    Generate fake Zip Code using Random Lib
    :return: 10001
    """
    return random.randrange(10000, 99999)


def generate_phone():
    """
    Generate Phone using Random Lib
    :return: 9876543210
    """
    return random.randrange(1000000000, 9999999999)


def generate_ssn():
    """
    Generate fake SSN using Faker Lib
    :return: 908-89-1234
    """
    return fake.ssn()


def generate_address():
    """
    Generate Street Address line 1 using Faker Lib
    :return: 831 Allen Rd.
    """
    return fake.street_address()


def generate_city():
    """Generate City  using Faker Lib
    :return: Dayton
    """
    return fake.city()


def generate_secondary_address():
    """
    Generate street address line 2 using Faker Lib
    :return: fort
    """
    return fake.city_suffix()


def generate_date_of_birth():
    """
    Generate Date of Birth in mmddyy using Faker Lib
    :return: 09/12/1987
    """
    return fake.date_of_birth(minimum_age=21, maximum_age=80).strftime('%m/%d/%Y')


def generate_unix_timestamp():
    """
    The function generates a Unix timestamp based on a fake date and time.
    :return: a Unix timestamp, which is the number of seconds that have elapsed since January 1, 1970,
    at 00:00:00 UTC.
    """
    fake_date_time = fake.date_time_this_decade()
    unix_timestamp = int(time.mktime(fake_date_time.timetuple()))
    return unix_timestamp


def generate_unix_timestamp_millisec():
    """
    The function generates a Unix timestamp in milliseconds.
    :return: a Unix timestamp in milliseconds.
    """
    today = datetime.now()
    one_month_from_now = today + timedelta(days=30)
    random_date = fake.date_time_between(start_date=today, end_date=one_month_from_now)
    unix_timestamp = int(random_date.timestamp()) * 1000
    return unix_timestamp


def generate_current_unix_time_milisec():
    """
    """
    today_date = datetime.now()
    unix_timestamp_milliseconds = int(today_date.timestamp() * 1000)
    print(unix_timestamp_milliseconds)
    return unix_timestamp_milliseconds


def fake_unix_timestamp_with_week_offset(week_offset):
    current_time = datetime.now()
    target_time = current_time + timedelta(weeks=week_offset)
    unix_timestamp = int(target_time.timestamp()) * 1000
    return unix_timestamp


def generate_next_year_unix_timestamp_millisec():
    """
    """
    random_date_this_year = fake.date_time_this_year()
    next_year = datetime.now().year + 1
    tomorrow = datetime.now() + timedelta(days=1)
    next_year_date = random_date_this_year.replace(year=next_year, month=tomorrow.month, day=tomorrow.day,
                                                   hour=tomorrow.hour, minute=tomorrow.minute, second=tomorrow.second)
    unix_timestamp = int(next_year_date.timestamp() * 1000)
    print(unix_timestamp)
    return unix_timestamp


def generate_routing_number():
    """
    Generate Bank Routing Number using Faker Lib
    :return: 082333643
    """
    return fake.aba()


def generate_bank_account_number():
    """
    Generate Basic Bank Account Number using Faker Lib
    :return: WRRB23520835508179
    """
    return fake.bban()


def generate_advertiser_name():
    return fake.company()


def generate_contract_name():
    """
    Generate Financial Institution Name using Faker Lib
    :return: monetize compelling systems bank
    """
    return fake.bs()


def generate_product_name():
    """
    Generate Financial Institution Name using Faker Lib
    :return: monetize compelling systems bank
    """
    return fake.bs()


def generate_contract_description():
    """
    Generate Financial Institution Name using Faker Lib
    :return: monetize compelling systems bank
    """
    return fake.bs()


def generate_country_name():
    """
    Generate Financial Institution Name using Faker Lib
    :return: monetize compelling systems bank
    """
    return fake.country()


def generate_url():
    """The function `generate_url` returns a randomly generated URL.
    :return: a randomly generated URL.
    """
    return fake.url()


def generate_fake_logo_name():
    adjectives = ['Dynamic', 'Innovative', 'Elegant', 'Modern', 'Sleek', 'Bold', 'Vibrant', 'Creative', 'Striking']
    nouns = ['Solutions', 'Technologies', 'Innovations', 'Designs', 'Systems', 'Creations', 'Ventures', 'Labs',
             'Studios']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f'{adjective} {noun} Logo'


def generate_popup_text(min_words=10, max_words=30):
    """
    """
    num_words = random.randint(min_words, max_words)
    fake_text = fake.texts(nb_texts=1, max_nb_chars=num_words * 5)[0]
    return ' '.join(fake_text.split()[:num_words])


def generate_tag_name():
    """
    Generate Financial Institution Name using Faker Lib
    :return: monetize compelling systems bank
    """
    return fake.word()


def generate_fake_tagline():
    """
    """
    return fake.catch_phrase()


def generate_advertising_description():
    """
    generate fake sentese
    """
    return fake.sentence()


def generate_email_offer_text():
    product = fake.word()
    discount = fake.random_int(min=5, max=50)
    expiration_date = fake.date_this_month(after_today=True).strftime("%B %d, %Y")
    message = f"Exclusive Offer Alert!\n\nGet {discount}% off on our {product}! Hurry, this offer expires on {expiration_date}. Visit our website now!\n\nHappy Shopping!"
    return message


def generate_campaign_name():
    return fake.catch_phrase()


def generate_campaign_description():
    return fake.paragraph(nb_sentences=3)


def generate_no_of_period():
    random_number = random.randint(1, 12)
    return random_number


def generate_total_budget_amt():
    total_budget_amt = random.randint(10000, 500000)
    return total_budget_amt


def generate_content_id():
    random_number = random.randint(111, 9999)
    return random_number
