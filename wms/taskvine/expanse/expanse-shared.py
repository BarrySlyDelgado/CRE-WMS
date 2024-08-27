import ndcctools.taskvine as vine
import argparse


def write_file(filename, size):
    with open(filename, "wb") as f:
        f.write(b"0"*size)

def read_file(filename):
    data = open(filename, "rb").read()

def main():
    
    m = vine.Manager()
    m.set_name("taskvine_expanse_workflow")
    m.tune("wait-for-workers", args.workers)

    temp_files = [] 
    for i in range(args.producer_ratio):
        filename = f"/p/lustre1/slydelgado1//filename_{i}"
        temp_files.append(filename)
        t = vine.PythonTask(write_file, filename, args.bytes)
        t.set_cores(1)
        t.set_category("write")
        m.submit(t)
    
    while not m.empty():
        t = m.wait(5)
        if t:
            pass

    for infile in temp_files:
        for _ in range(args.consumer_ratio):
            t = vine.PythonTask(read_file, infile)
            t.set_cores(1)
            t.set_category("read")
            m.submit(t)

    while not m.empty():
        t = m.wait(5)
        if t:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="TaskVine Expanse Example",
                            description="ephemeral data example")
    
    parser.add_argument("-N", "--producer-ratio", default=1, type=int)
    parser.add_argument("-M", "--consumer-ratio", default=1, type=int)
    parser.add_argument("-B", "--bytes", default=1024, type=int)
    parser.add_argument("-W", "--workers", default=1, type=int)
    args = parser.parse_args()
    main()
        
