
def thank(fx):
    def mfx(*args, **kwargs):
        fx(*args, **kwargs)
        print("Thank you everyone")
    return mfx
@thank
def hello():
    print("Hello world")
# thank(hello)()

@thank
def add(a, b , c):
    print(a+b+c)


hello()
add(5,3,6)
