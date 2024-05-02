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
    if rasp:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        click.echo(line)
        click.echo(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        click.echo(line)
        for idx, worker in enumerate(rasp, 1):
            click.echo(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    worker.get('punkt', ''),
                    worker.get('number', ''),
                    worker.get('time', 0)
                )
            )
            click.echo(line)
    else:
        click.echo("Расписание пусто.")


def select_trains(rasp, number):
    result = []
    for d in rasp:
        if number in d.values():
            result.append(d)
        else:
            continue
    return result


def save_trains(file_name, rasp):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(rasp, fout, ensure_ascii=False, indent=4)


def load_trains(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "r", encoding="utf-8") as fin:
            return json.load(fin)
    else:
        return []


@click.command()
@click.argument("filename", required=True)
@click.option("--punkt", help="The punkt's name")
@click.option("--number", help="The train's number")
@click.option("--time", help="The time of otpravlenie")
@click.option("--number_train", help="The required numbers")
def main(filename, punkt, number, time, number_train):
    rasp = load_trains(filename)

    if punkt and time:
        rasp = add_train(rasp, punkt, number, time)
        save_trains(filename, rasp)
    elif number_train:
        selected = select_trains(rasp, number_train)
        display_train(selected)
    else:
        display_train(rasp)


if __name__ == "__main__":
    main()
