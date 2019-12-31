def data_minify(file_name):
    with open(f'./{file_name}') as file, open('./small_reviews.csv', 'w') as output:
        for _ in range(10_000):
            output.write(file.readline())
if __name__ == "__main__":
    file_name = input('Please enter a file name: ')
    data_minify(file_name)