from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def run_tests():
    # get_files_info tests
    print("Test 1: get_files_info('calculator', '.')")
    print(get_files_info("calculator", "."))
    print("\nTest 2: get_files_info('calculator', 'pkg')")
    print(get_files_info("calculator", "pkg"))
    print("\nTest 3: get_files_info('calculator', '/bin')")
    print(get_files_info("calculator", "/bin"))
    print("\nTest 4: get_files_info('calculator', '../')")
    print(get_files_info("calculator", "../"))

    # get_file_content tests
    print("\nTest 5: get_file_content('calculator', 'main.py')")
    print(get_file_content("calculator", "main.py"))
    print("\nTest 6: get_file_content('calculator', 'pkg/calculator.py')")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\nTest 7: get_file_content('calculator', '/bin/cat')")
    print(get_file_content("calculator", "/bin/cat"))

    # write_file tests
    print("\nTest 8: get_file_content('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("\nTest 9: get_file_content('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("\nTest 10: get_file_content('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    # run_python_file tests
    print("\nTest 11: run_python_file('calculator', 'main.py')")
    print(run_python_file("calculator", "main.py"))
    print("\nTest 12: run_python_file('calculator', 'tests.py')")
    print(run_python_file("calculator", "tests.py"))
    print("\nTest 13: run_python_file('calculator', '../main.py')")
    print(run_python_file("calculator", "../main.py"))
    print("\nTest 14: run_python_file('calculator', 'nonexistent.py')")
    print(run_python_file("calculator", "nonexistent.py"))

    # call_function tests
    print("\nTest 15: call_function('get_files_info', {'directory': '.'})")
    print(get_files_info("calculator", "."))
    print("\nTest 16: call_function('get_file_content', {'file_path': 'main.py'})")
    print(get_file_content("calculator", "main.py"))
    print("\nTest 17: call_function('write_file', {'file_path': 'test.txt', 'content': 'Hello World!'})")
    print(write_file("calculator", "test.txt", "Hello World!"))
    print("\nTest 18: call_function('run_python_file', {'file_path': 'main.py'})")
    print(run_python_file("calculator", "main.py"))

if __name__ == "__main__":
    run_tests()
