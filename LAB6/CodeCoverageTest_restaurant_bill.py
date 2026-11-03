import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# Starter tests
def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_even_split():
    assert split_bill(1000, 4, 10) == 275


# bill_total
def test_unknown_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("patio", 100, 2, False)


def test_negative_food_total():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -1, 2, False)


def test_zero_guests():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 100, 0, False)


def test_happy_hour_discount():
    # 1000 -> 800, service 80, total 880, +5% = 924
    assert bill_total("dine_in", 1000, 2, True) == 924


def test_large_party_surcharge():
    # service 100 + 200 = 300, total 1300, +5% = 1365
    assert bill_total("dine_in", 1000, 8, False) == 1365


# split_bill
def test_split_zero_people():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)


def test_split_negative_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)


def test_split_rounds_up():
    # 1000 / 3 = 333 remainder 1, so the share is 334
    assert split_bill(1000, 3, 0) == 334


# table_wait
def test_large_party_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"


def test_reservation_seats_now():
    assert table_wait(4, 0, True) == "seat now"


def test_no_free_tables_waitlist():
    assert table_wait(4, 0, False) == "waitlist"


def test_big_party_few_tables_waitlist():
    assert table_wait(8, 1, False) == "waitlist"


def test_seat_now_default():
    assert table_wait(4, 3, False) == "seat now"