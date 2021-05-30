import json
import datetime


def filter_by_date_range(input_dict, start, end):
    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict['items']
                   if get_date_obj(x['date']) >= get_date_obj(start)
                   and get_date_obj(x['endDate']) <= get_date_obj(end)]
    # Transform python object back into json
    return output_dict


def filter_by_id(input_dict, event_id):
    output_dict = [x for x in input_dict['items'] if x['id'] == event_id]
    if len(output_dict) == 0:
        return {}
    else:
        return output_dict[0]


def filter_by_venue_name(input_dict, venue_name):
    output_dict = [x for x in input_dict['items'] if x['title'] == venue_name]
    if len(output_dict) == 0:
        return {}
    else:
        return output_dict[0]


def get_date_obj(date_str):
    # 2021-02-01T03:00:00+01:00
    # 2021-02-01
    date_part_only = date_str
    if 'T' in date_str:
        date_part_only = date_str.split('T')[0]
    date_parts = date_part_only.split('-')
    return datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False
