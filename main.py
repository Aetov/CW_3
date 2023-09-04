from utils import get_data, get_filtered_data, get_last_values, get_formatted_data

def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_formatted_data(data)
    print('INFO: Вывод тразакций...')
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()