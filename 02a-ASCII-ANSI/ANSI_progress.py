import time
import sys


def somework(i, duration=0.25):
    time.sleep(duration)

class ANSI:
    reset = '\u001b[0m'
    red = '\u001b[31m'
    upby = lambda n: '\u001b[{}A'.format(n)
    downby = lambda n: '\u001b[{}B'.format(n)
    leftby = lambda n: '\u001b[{}D'.format(n)


def progress2line():
    # Нам нужно две строки, одна есть, вторую оставим пока пустой
    sys.stdout.write('\n')

    bar_total_len = 40
    done_char = '■'  # U+25A0 'Black Square'
    todo_char = ' '  # Space

    work = range(543)
    for job in work:
        done_frac = round(job/len(work), ndigits=2)
        todo_frac = 1 - done_frac

        done_len = round(bar_total_len * done_frac)
        todo_len = bar_total_len - done_len

        # Встаём в самое начало (верхний левый угол)
        sys.stdout.write(ANSI.leftby(100))  # Можно и поточнее посчитать сдвиг
        sys.stdout.write(ANSI.upby(1))

        sys.stdout.write("{:5.1f}%".format(round(100*done_frac, ndigits=1)))

        # Опускаемся в начало второй строки
        sys.stdout.write(ANSI.leftby(100))
        sys.stdout.write(ANSI.downby(1))
        sys.stdout.write(
            "|{done}{todo}|".format(
                done=done_len*done_char,
                todo=todo_len*todo_char
            )
        )
        sys.stdout.flush()

        somework(job, duration=0.01)
    print()

progress2line()
