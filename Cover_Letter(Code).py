import time

def type_writer(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run_interactive_intro():
    type_writer("Name: Sunghyuk Yoon")
    time.sleep(0.5)

    type_writer("Trait: Fast learner, Machine Learning & Deep Learning, C++, Python")
    time.sleep(0.5)

    type_writer("Education: UCLA, Electrical and Computer Engineering")
    time.sleep(0.5)

    type_writer("Work: AmazeVR, C++, algorithm problem solving")
    time.sleep(2)
    
    print("")
    type_writer("Applying....")
    print("")
    time.sleep(2)

    type_writer("epoch 1..")
    time.sleep(1.5)
    type_writer("epoch 2..")
    time.sleep(1.5)
    type_writer("epoch 3..")
    time.sleep(2)
    type_writer("Trained rate: 100% !")
    time.sleep(1)
    print("")
    
    type_writer("Final reward !!")
    print()

    print("")
    type_writer("Design isn’t how something looks.", delay=0.05)
    time.sleep(0.5)
    type_writer("It’s how it works, how it’s built, and how it makes people feel.", delay=0.05)
    time.sleep(0.5)
    print()
    type_writer("That’s why I want to build for Apple.", delay=0.07)

run_interactive_intro()
time.sleep(5)