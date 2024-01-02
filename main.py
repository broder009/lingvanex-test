from filter import concatenate, create_output, read_data

def main():
    source, target = read_data()
    result = concatenate(source=source, target=target)
    create_output(result=result)

if __name__ == '__main__':
    main()
