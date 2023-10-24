def sorting_list():
    to_do_list = []
    while True:
        job = input()
        if job == 'End':
            break
        to_do_list.append(job)
    to_do_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
    final_to_do_list = [note.split('-')[1] for note in to_do_list]
    return final_to_do_list

print(sorting_list())