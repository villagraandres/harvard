def announce(f):
    def wrapper():
        print("about to run the function");
        f();
        print("done");
    return wrapper

@announce
def hello():
    print("hello michi!");

hello();