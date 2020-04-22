import gpxpy


def readgpx(file):
    gpx = gpxpy.parse(file)
    track = gpx.tracks[0]
    segment = track.segments[0]
    data = []
    for idx, point in enumerate(segment.points):
        data.append([point.time, segment.get_speed(idx),
                     point.longitude, point.latitude, point.elevation])
    col = ["time", "speed", "longitude", "latitude", "Altitude"]
    return col, data


if __name__ == "__main__":
    with open("./data/2020-03-12_12-29-59.gpx", encoding="UTF-8") as gpxfile:
        col, data = readgpx(gpxfile)
