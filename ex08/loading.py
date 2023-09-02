def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, 1):
        percentage = (i / total) * 100
        yield item
        progress = f"{int(percentage)}%|[{'=' * int(percentage / 2)}{'>' if percentage < 100 else ''}{' ' * (50 - int(percentage / 2))}]| {i}/{total}"
        print(progress, end='\r')
