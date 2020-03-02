from weather import weather


def main():
    source_path = "data_files/csv_weather_data/"
    destination_path = "data_files/parquet_weather_data/"

    weather_results = weather.Weather(source_path, destination_path)
    return print(weather_results.get_results())


if __name__ == '__main__':
    main()
