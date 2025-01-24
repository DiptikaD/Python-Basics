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

def extend_route_information(route, more_route_information):
    combined = {**route, **more_route_information}
    return combined
    
def fix_wagon_depot(wagons_rows):
    transposed = list(zip(*wagons_rows))
    ## zip allows for looping over 2 or more iterables at the same time, 
    # is an alternative to looping with indexes

    return [list(row) for row in transposed]
