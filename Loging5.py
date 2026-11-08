def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
    except AssertionError as e:
        print(e)
    else:
        print(f"Список містить {len(input_list)} елементів")

process_list([1, 2, 3])