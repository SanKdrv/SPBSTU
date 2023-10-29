def find_common_participants(first_group, second_group, spliter=","):
    first_group = list(first_group.split(spliter))
    second_group = list(second_group.split(spliter))
    return sorted(list(set(first_group).intersection(second_group)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
