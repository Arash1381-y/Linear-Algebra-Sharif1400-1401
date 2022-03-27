import numpy as np


class City:
    def __init__(self, number):
        self.number = number
        self.cities = []
        self.border_cities = []
        self.hull = []
        self.cities_number = 0
        self.center = None

    def build_convex(self):
        self.hull.clear()
        left_most_index = 0
        for i in range(1, self.cities_number):
            if self.cities[i][0] < self.cities[left_most_index][0]:
                left_most_index = i
            elif self.cities[i][0] == self.cities[left_most_index][0]:
                if self.cities[i][1] > self.cities[left_most_index][1]:
                    left_most_index = i

        current_point_index = left_most_index
        while True:
            self.hull.append(self.cities[current_point_index])
            point_two_index = (current_point_index + 1) % self.cities_number
            for i in range(self.cities_number):
                if orientation(self.cities[current_point_index], self.cities[i], self.cities[point_two_index]) < 0:
                    point_two_index = i

            current_point_index = point_two_index

            if point_two_index == left_most_index:
                break

        self.center = np.sum(self.hull, axis=0) * (1 / len(self.hull))

    def add_city(self, new_city):
        self.cities.append(new_city)
        self.cities_number += 1


def orientation(point_one, point_two, point_three):
    val = (point_two[1] - point_one[1]) * (point_three[0] - point_two[0]) \
          - (point_three[1] - point_two[1]) * (point_two[0] - point_one[0])

    return val


def init_countries(count_city, count_country, countries):
    for i in range(count_country):
        countries.append(City(i))
    for i in range(count_city):
        country_num, longitude, latitude = input().split()
        country_num, longitude, latitude = [int(country_num), float(longitude), float(latitude)]
        vector = np.array([longitude, latitude])
        countries[country_num].add_city(vector)


def choose_closest_country(countries, new_cities_num, selected_countries):
    for i in range(new_cities_num):
        longitude, latitude = input().split()
        longitude, latitude = [float(longitude), float(latitude)]
        vector = np.array([longitude, latitude])

        dist = None
        most_close_city = countries[0]

        for country in countries:
            new_dist = np.linalg.norm(vector - country.center)
            if dist is not None:
                if dist > new_dist:
                    dist = new_dist
                    most_close_city = country
            else:
                dist = np.linalg.norm(vector - country.center)
                most_close_city = country

        most_close_city.add_city(vector)
        most_close_city.build_convex()
        selected_countries.append(most_close_city.number)


def print_result(countries, selected_countries):
    print(*selected_countries)
    for country in countries:
        country.hull.sort(key=lambda x: (x[0], x[1]), reverse=False)
        print(country.number, end=" ")
        for element in country.hull:
            format_vector_x = "{:.2f}".format(element[0])
            format_vector_y = "{:.2f}".format(element[1])
            print(f"[{format_vector_x}, {format_vector_y}]", end=" ")
        print()


def main():
    count_city, count_country = input().split()
    count_city, count_country = [int(count_city), int(count_country)]
    countries = []
    init_countries(count_city, count_country, countries)

    for country in countries:
        country.build_convex()

    new_cities_num = int(input())
    selected_countries = []
    choose_closest_country(countries, new_cities_num, selected_countries)

    print_result(countries, selected_countries)


if __name__ == "__main__":
    main()
