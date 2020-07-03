

def get_popular_times ():
    # need to figure out how to use external libraries with vercel
    import populartimes
    import json

    api_key = "AIzaSyARbfAurhEXFsuEp1SvJlq6OieCqPvpxWg"
    #Trinity Bellwood Park PlaceID
    place_id_1 = "ChIJ29zuWfs0K4gRu3X7rsgi-wM"
    #Fill These out with the actual park
    # https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder
    place_id_2 = "ChIJ29zuWfs0K4gRu3X7rsgi-wM"
    place_id_3 = "ChIJ29zuWfs0K4gRu3X7rsgi-wM"
    place_id_4 = "ChIJ29zuWfs0K4gRu3X7rsgi-wM"

    list_of_place_ids = [place_id_1,place_id_2, place_id_3, place_id_4]
    list_of_place_popularity = []
    for place_id in list_of_place_ids:
      response = populartimes.get_id(api_key, place_id)
      current_popularity = response["current_popularity"]
      name = response["name"]
      is_busy = current_popularity > 50

      place_info = {
          "current_popularity": current_popularity,
          "name": name,
          "is_busy": is_busy
      }
      list_of_place_popularity.append(place_info)

    #return list of place popularity info as a json
    return json.dumps(list_of_place_popularity)