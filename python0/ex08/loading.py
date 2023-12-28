import sys
from tqdm import tqdm
from time import sleep

def print_progress(current, total):
        percent = (current / total) * 100
        bar_length = 50
        bar = "=" * int(bar_length * current / total) + ">"
        
        sys.stdout.write(f"\r{int(percent)}%|[{bar.ljust(bar_length)}]| {current}/{total}")
        sys.stdout.flush()

def ft_tqdm(lst: range) -> None:
    total = len(lst)

    if total == 0:
        return

    for i, item in enumerate(lst):
        yield item
        print_progress(i + 1, total)
    print()

def main():
    if len(sys.argv) != 1:
        print("Usage: python loading.py")
        sys.exit()

    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in tqdm(range(333)):
        sleep(0.005)
    print()

if __name__ == "__main__":
    main()
