def get_list_of_wagons(*args):
    *values, = args
    return values

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first, second, third, *rest = each_wagons_id
    *combined, = third, *missing_wagons, *rest, first, second 
    # NOTE FOR ABOVE: the items with the * are the because they are a list/tuple, not just one value
    return combined

def add_missing_stops(route, **kwargs):

    stops = list(kwargs.values())
    route["stops"] = stops
    
    return route