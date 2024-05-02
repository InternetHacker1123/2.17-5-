#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import click
import json
import os.path


def add_train(rasp, punkt, number, time):
    """
   Добавить данные о работнике.
   """
    rasp.append(
        {
            "punkt": punkt,
            "number": number,
            "time": time
        }
    )
    return rasp


def display_train(rasp):
    """
   Отобразить список работников.
   """
    # Проверить, что список работников не пуст.
    if rasp:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(rasp, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    worker.get('punkt', ''),
                    worker.get('number', ''),
                    worker.get('time', 0)
                )
            )
            print(line)
    else:
        print("Расписание пусто.")


def select_trains(rasp, number):
    result = []
    for d in rasp:
        if number in d.values():
            result.append(d)
        else:
            print('Поезда с таким номером нет')
        return result


def save_trains(file_name, rasp):
    # Сохранить всех работников в файл JSON.
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(rasp, fout, ensure_ascii=False, indent=4)


def load_trains(file_name):
    """
   Загрузить всех работников из файла JSON.
   """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main(command_line=None):


@click.group()
def trains():
    pass


@trains.command()
@click.argument("filename", type=click.Path())
@click.option("-p", "--punkt", required=True, help="The punkt's name")
@click.option("-n", "--number", help="The train's number")
@click.option("-t", "--time", required=True, help="The time of otpravlenie")
def add(filename, punkt, number, time):
    click.echo(
        f"Adding a new train: Punkt - {punkt}, Number - {number}, Time - {time}")


@trains.command()
@click.argument("filename", type=click.Path())
def display(filename):
    click.echo("Displaying all trains")


@trains.command()
@click.argument("filename", type=click.Path())
@click.option("-nt", "--number_train", required=True, help="The required numbers")
def select(filename, number_train):
    click.echo(f"Selecting the trains with number: {number_train}")


if __name__ == "__main__":
    trains()
